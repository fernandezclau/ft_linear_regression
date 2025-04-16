# ft_linear_regression

A minimal end-to-end implementation of simple linear regression, including data loading, model training, evaluation, and a lightweight web interface for visualization.

## Features
1. Load and preprocess your dataset.
2. Train a simple linear regression model using scikit-learn.
3. Visualize predictions and model performance through a clean web interface.
4. Run basic tests to verify functionality.

## Technologies
- Python 3.13 
- Flask 
- NumPy, Pandas 
- HTML/CSS (Jinja2 templates)

## Project Structure

```
linear_regression/
  app.py             # Web application (Flask)
  data.py            # Data handling utilities
  model.py           # Linear regression model
  train.py           # Model training script
  test.py            # Basic tests
  static/            # Static files (CSS, JS, images)
  templates/         # HTML templates
  data/              # Dataset files
  requirements.txt   # Project dependencies
  README.md          # Project documentation
```
## Getting Started

### Clone the Repository

```bash
  git clone https://github.com/your_username/linear_regression.git
  
  cd linear_regression
```

### Install Dependencies
It's recommended to use a virtual environment.
```bash
  python -m venv .venv
```
```bash
  source .venv/bin/activate    # Linux/macOS
```
```bash
  .venv\Scripts\activate       # Windows
```
```bash
  pip install -r requirements.txt
```

## Train the Model
```bash
  python train.py
```
## Run the Web Application
```bash
    python app.py
```

Access the app at http://127.0.0.1:5000

# Why This Project Exists
This is a focused, clean example of implementing a machine learning workflow from scratch, with no unnecessary libraries
or overengineering. It’s meant for those who want to understand how each piece fits together — from raw data to a 
running app.
