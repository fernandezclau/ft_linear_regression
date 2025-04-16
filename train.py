from model import LinearRegression
from data import DataFormatter

formatter = DataFormatter(csv='./data/data.csv')

x = formatter.x_scaled
y = formatter.y_scaled

# 1. Train model
model = LinearRegression(learning_rate=0.01, iterations=1000)
model.train(x, y)

# 2. Save model
model.save_model()


