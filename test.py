import numpy as np
from sklearn.linear_model import LinearRegression as SklearnLR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from data import DataFormatter
from model import LinearRegression # My implementation

# Load data
formatter = DataFormatter(csv='./data/data.csv')

x = formatter.x_scaled
y = formatter.y_scaled

# ---- 1. SHOW DATA ----
formatter.show_data()

# ---- 1. TRAIN MODELS ----
# My model
model = LinearRegression()
model.train(x, y)
model.save_model()
#model.load_model()

# Scikit-learn model
sklearn_model = SklearnLR()
sklearn_model.fit(x.reshape(-1, 1), y)

# Compare theta results
print(f"My model - theta0: {model.theta0}, theta1: {model.theta1}")
print(f"Sklearn model - theta0: {sklearn_model.intercept_}, theta1: {sklearn_model.coef_[0]}")

# ---- 2. COMPARE MSE AND R² ----
# My model
y_pred = model.predict(x)
mse_my_model, mae_my_model = model.compute_loss(x, y)
r2_my_model = model.compute_r2(x, y)

# Scikit-learn model
y_pred_sklearn = sklearn_model.predict(x.reshape(-1, 1))
mse_sklearn = mean_squared_error(y, y_pred_sklearn)
mae_sklearn = mean_absolute_error(y, y_pred_sklearn)
r2_sklearn = r2_score(y, y_pred_sklearn)

# Compare values
print(f"MSE my model: {mse_my_model:.6f}")
print(f"MAE my model: {mae_my_model:.6f}")
print(f"R² my model: {r2_my_model:.6f}")
print(f"MSE sklearn: {mse_sklearn:.6f}")
print(f"MAE sklearn: {mae_sklearn:.6f}")
print(f"R² sklearn: {r2_sklearn:.6f}")

# ---- 3. COMPARE REAL VALUES ---
real_mileages = [20000, 50000, 100000]
real_mileages_scaled = formatter.normalize_input(real_mileages)

# My model
predictions_your_model = model.predict(real_mileages_scaled)

# Scikit-learn model
predictions_sklearn = sklearn_model.predict(np.array(real_mileages_scaled).reshape(-1, 1))

print("\nPredictions:")
for i, km in enumerate(real_mileages):
    print(f"  {km} km ➝ My model: {predictions_your_model[i]:.4f} | sklearn: {predictions_sklearn[i]:.4f}")
