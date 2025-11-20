import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("temperature_anomaly.csv")

# Keep only needed columns
data = data[data["Entity"] == "World"]
print(data)
data = data[["Year", "Global average temperature anomaly relative to 1861-1890"]]
data.columns = ["Year", "Anomaly"]

# Clean
data = data.sort_values("Year")
data["Anomaly"] = pd.to_numeric(data["Anomaly"], errors="coerce")
data = data.dropna()


# Keep only the last 100 years
last_100_years = data[data["Year"] >= data["Year"].max() - 100]

# Split: first 90 years for training, last 10 for testing
train = last_100_years.iloc[:-10]   # everything except last 10
test  = last_100_years.iloc[-10:]   # last 10 rows

x_train = train["Year"].values
y_train = train["Anomaly"].values

x_test = test["Year"].values
y_test = test["Anomaly"].values

results = {}

degree = 6

# Get coefficients AND covariance matrix
coeffs, cov = np.polyfit(x_train, y_train, degree, cov=True)
poly_model = np.poly1d(coeffs)

# Predictions
y_pred_train = poly_model(x_train)
y_pred_test  = poly_model(x_test)

# Error on test set
rmse = np.sqrt(np.mean((y_pred_test - y_test)**2))

results[degree] = {
    "model": poly_model,
    "rmse": rmse,
    "pred_train": y_pred_train,
    "pred_test": y_pred_test,
    "coeffs": coeffs,
    "covariance_matrix": cov
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
plt.title("Polynomial Forecasts (Degree 6)")
plt.legend()
plt.show()

all_tables = []

for degree, info in results.items():
    df_train = pd.DataFrame({
        "Degree": [degree] * len(x_train),
        "Year": x_train,
        "Actual": y_train,
        "Predicted": info["model"](x_train)   # FIX: compute predictions here
    })
    all_tables.append(df_train)

# Concatenate into one big DataFrame
final_df = pd.concat(all_tables, ignore_index=True)

# Save to CSV
#final_df.to_csv("all_poly_fits.csv", index=False)

print("Covariance matrix for degree 6:")
print(results[6]["covariance_matrix"])
