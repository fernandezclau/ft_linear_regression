import numpy as np
import pandas as pd


class DataFormatter:

    def __init__(self, csv, x_title=None, y_title=None, title=None):
        self.title = title
        self.x_title = x_title
        self.y_title = y_title
        self.__get_csv_data(csv)
        self.__scale_data()

    def format_data(self, filename="./data/parameters.csv") -> dict:
        info = dict()
        df = None

        if filename:
            try:
                df = pd.read_csv(filename)
            except Exception as e:
                print(f"Error loading the file: {e}")

        info["description"] = {
            "title": self.title,
            "x_title": self.x_title,
            "y_title": self.y_title
        }
        info["training_data"] = list(zip(self.x_train, self.y_train))  # Convierte los datos a listas
        if df is not None:
            info["regression_line"] = {
                "slope": float(df['theta0'].iloc[0]),
                "intercept": float(df['theta1'].iloc[0])
            }
            info["metrics"] = {
                "learning_rate": float(df['learning_rate'].iloc[0]),
                "iterations": float(df['iterations'].iloc[0]),
                "mse": float(df['mse'].iloc[0]),
                "r2": float(df['r2'].iloc[0])
            }

        info["scaling"] = {
            "x_scaled": self.x_scaled.tolist(),
            "y_scaled": self.y_scaled.tolist(),
            "x_mean": float(self.x_mean),
            "x_std": float(self.x_std),
            "y_mean": float(self.y_mean),
            "y_std": float(self.y_std)
        }

        return info

    def __scale_data(self):
        self.x_mean = np.mean(self.x_train)
        self.x_std = np.std(self.x_train)
        self.x_scaled = (self.x_train - self.x_mean) / self.x_std

        self.y_mean = np.mean(self.y_train)
        self.y_std = np.std(self.y_train)
        self.y_scaled = (self.y_train - self.y_mean) / self.y_std

    def normalize_input(self, x):
        x_mean = np.mean(self.x_train)
        x_std = np.std(self.x_train)
        x1_normalized = (x - x_mean) / x_std
        return x1_normalized

    def denormalize_output(self, y):
        y_mean = np.mean(self.y_train)
        y_std = np.std(self.y_train)
        y_denormalized = y * y_std + y_mean
        return y_denormalized

    def __get_csv_data(self, csv: str):
        df = None

        try:
            df = pd.read_csv(csv)
        except Exception as e:
            print(f"Error loading the file: {e}")

        if df is not None:
            self.x_train = df['km'].values.tolist()
            self.y_train = df['price'].values.tolist()
