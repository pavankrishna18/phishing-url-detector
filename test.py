import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset (X = study hours, y = scores)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5, 7])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Calculate residuals
residuals = y - y_pred

# Plot regression line
plt.subplot(2, 1, 1)
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()

# Plot residuals
plt.subplot(2, 1, 2)
plt.scatter(X, residuals, color="green")
plt.axhline(y=0, color="red", linestyle="--")
plt.title("Residual Plot")
plt.xlabel("X")
plt.ylabel("Residuals")

plt.tight_layout()
plt.show()
