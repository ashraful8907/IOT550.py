import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("temperature_anomaly.csv")

# Keep only needed columns
data = data[["Year", "Global average temperature anomaly relative to 1861-1890"]]
data.columns = ["Year", "Anomaly"]

# Clean
data = data.sort_values("Year")
data["Anomaly"] = pd.to_numeric(data["Anomaly"], errors="coerce")
data = data.dropna()


cutoff = data["Year"].max() - 10

train = data[data["Year"] <= cutoff]
test  = data[data["Year"] > cutoff]

x_train = train["Year"].values
y_train = train["Anomaly"].values

x_test = test["Year"].values
y_test = test["Anomaly"].values

# ---------------------------
# 3. FIT POLYNOMIALS DEGREE 1–9
# ---------------------------

results = {}

for degree in range(1, 10):
    coeffs = np.polyfit(x_train, y_train, degree) # Fitting polynomials degree 1-10
    poly_model = np.poly1d(coeffs)

    # Predict the last 10 years (testing)
    y_pred_test = poly_model(x_test)

    # Compute error
    rmse = np.sqrt(np.mean((y_pred_test - y_test)**2))

    # Store results
    results[degree] = {
        "model": poly_model,
        "rmse": rmse
    }


x_future = np.arange(train["Year"].max() + 1, train["Year"].max() + 11)

plt.figure(figsize=(12, 7))

plt.scatter(x_train, y_train, label="Training Data")
plt.scatter(x_test, y_test, label="Test Data")

for degree in results:
    model = results[degree]["model"]
    plt.plot(x_future, model(x_future), linestyle="--", label=f"Forecast deg {degree}")

plt.xlabel("Year")
plt.ylabel("Temperature Anomaly")
plt.title("Polynomial Forecasts (Degrees 1–9)")
plt.legend()
plt.show()

for degree, info in results.items():
    print(f"Degree {degree}: RMSE = {info['rmse']:.4f}")
