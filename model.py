import csv

import numpy as np


class LinearRegression:
    """
    A simple implementation of the Linear Regression model.
    The model is defined as: y = θ0 + θ1 * x where:
     - y is the predicted value,
     - θ0 is the intercept (y-intercept),
     - θ1 is the slope (coefficient),
     - x is the input feature.
    """

    def __init__(self, learning_rate=0.01, iterations=1000, filename="./data/parameters.csv"):
        """
        Initialize the model with hyperparameters and file path.
        :param learning_rate: The rate at which the model learns during training.
        :param iterations: The number of iterations to run the gradient descent.
        :param filename: The file path to save and load the model parameters.
        """
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.filename = filename
        self.theta0 = 0.0   # intercept (θ0)
        self.theta1 = 0.0   # slope (θ1)
        self.mse = None     # Mean Squared Error (MSE)
        self.mae = None     # Mean Absolute Error (MAE)
        self.r2 = None      # R-squared, will be calculated later

    def predict(self, x):
        """
        Predict the target variable y for a given input x.
        :param x: The input feature.
        :return: The predicted value(s) y.
        """
        return self.theta0 + self.theta1 * np.array(x)

    def train(self, x, y):
        """
        Train the linear regression model using gradient descent.
        :param x: The input feature values.
        :param y: The target output values.
        """
        x_len = len(x)

        for i in range(self.iterations):
            errors = self.predict(x) - y
            sum_errors = np.sum(errors)
            sum_errors_x = np.sum(errors * x)

            self.theta0 -= self.learning_rate * sum_errors / x_len
            self.theta1 -= self.learning_rate * sum_errors_x / x_len

            if i % (self.iterations // 10) == 0 or i == self.iterations - 1:
                loss_mse, loss_mae = self.compute_loss(x, y)
                print(f"Iteration {i}: Loss (MSE) = {loss_mse:.6f}")
                print(f"               Loss (MAE) = {loss_mae:.6f}")

        self.compute_r2(x, y)

    def compute_loss(self, x, y):
        """
        Compute the Mean Squared Error (MSE) and Mean Absolute Error (MAE).
        :param x: The input feature values.
        :param y: The true target values.
        :return: A tuple (MSE, MAE).
        """
        predictions = self.predict(x)
        errors = predictions - y
        self.mse = np.mean(errors ** 2)
        self.mae = np.mean(np.abs(errors))

        return self.mse, self.mae

    def compute_r2(self, x, y):
        """
        Compute the R-squared (R²) value, a statistical measure of the goodness of fit.
        :param x: The input feature values.
        :param y: The true target values.
        :return: The R-squared value.
        """
        predictions = self.predict(x)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - predictions) ** 2)
        self.r2 = 1 - (ss_residual / ss_total)
        return self.r2

    def save_model(self):
        """
        Save the model parameters (θ0, θ1) along with training settings and performance metrics to a CSV file.
        """
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['theta0', 'theta1', 'learning_rate', 'iterations', 'mse', 'mae', 'r2'])
            writer.writerow([self.theta0, self.theta1, self.learning_rate, self.iterations, self.mse, self.mae, self.r2])

    def load_model(self):
        """
        Load the model parameters (θ0, θ1) from a CSV file.
        """
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            params = next(reader)
            self.theta0, self.theta1 = float(params[0]), float(params[1])
            print(f'Model trained: theta0 = {self.theta0}, theta1 = {self.theta1}')
