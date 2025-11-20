import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("temperature_anomaly.csv")
data = data[["Year", "Global average temperature anomaly relative to 1861-1890"]]
data.columns = ["Year", "Anomaly"]

data = data.sort_values("Year")
data["Anomaly"] = pd.to_numeric(data["Anomaly"], errors="coerce")
data = data.dropna()

years = data["Year"].values
anoms = data["Anomaly"].values
n = len(anoms)   # number of datapoints

orders = range(1, 11)
dof_values = []  # DoF per polynomial

models = {}

for k in orders:
    # fit polynomial of degree k
    coeffs = np.polyfit(years, anoms, k)
    models[k] = np.poly1d(coeffs)

    # degrees of freedom: n - (k+1)
    dof = n - (k + 1)
    dof_values.append(dof)

# -----------------------------------
# 3. PLOT DEGREES OF FREEDOM vs POLY ORDER
# -----------------------------------
plt.figure(figsize=(8,5))
plt.plot(orders, dof_values, marker="o")
plt.xlabel("Polynomial Order")
plt.ylabel("Degrees of Freedom (n - (k+1))")
plt.title("Degrees of Freedom vs Polynomial Order")
plt.grid(True)
plt.show()
