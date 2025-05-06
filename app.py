from flask import Flask, render_template, request
from data import DataFormatter
from model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route to display the form and prediction results.
    Handles both GET (initial page load) and POST (form submission) requests.
    """

    # Create an instance of the DataFormatter to load and format data
    formatter = DataFormatter(
        x_title="Mileage (Km)",
        y_title="Price ($)",
        title="Price vs Mileage",
        csv='./data/data.csv'
    )

    model = LinearRegression()
    model.load_model()

    # Format the data (used for plotting and displaying)
    data = formatter.format_data()

    data['predicted_price'] = None
    if request.method == 'POST':
        try:
            # Get the input mileage
            x1 = float(request.form['x1'])

            if x1 < 0:
                raise ValueError

            x1_scaled = formatter.normalize_input(x1)
            predicted_price_scaled = model.predict([x1_scaled])[0]
            predicted_price = formatter.denormalize_output(predicted_price_scaled)

            data['predicted_price'] = round(predicted_price, 2)
            data['input_km'] = x1

        except ValueError:
            # If the input is not a valid number, display an error message
            data['predicted_price'] = "Enter a valid number."
            data['input_km'] = "N/A"

    # Render the template with the formatted data
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
