import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- Step 1: Generate synthetic data ----------
m_true = 2.0    # true slope
b_true = 5.0    # true intercept
n_points = 50
noise = 3

X = np.linspace(0, 10, n_points)
Y = m_true * X + b_true + np.random.normal(0, noise, n_points)

# Get absolute paths
import os

# Folder where this script resides
base_dir = os.path.dirname(os.path.abspath(__file__))  
csv_path = os.path.join(base_dir, 'synthetic_data.csv')
plot_path = os.path.join(base_dir, 'fit_plot.png')

# Save to CSV
data = pd.DataFrame({'X': X, 'Y': Y})
data.to_csv(csv_path, index=False)

# ---------- Step 2: Fit a line ----------
loaded_data = pd.read_csv(csv_path)
X_loaded = loaded_data['X']
Y_loaded = loaded_data['Y']

m_fit, b_fit = np.polyfit(X_loaded, Y_loaded, 1)

# ---------- Step 3: Plot ----------
plt.scatter(X_loaded, Y_loaded, label='Data', color='blue')
plt.plot(X_loaded, m_true * X_loaded + b_true, color='green', label='True Line')
plt.plot(X_loaded, m_fit * X_loaded + b_fit, color='red', label='Fitted Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Synthetic Data and Fitted Line')
plt.legend()

# Save the plot (absolute path)
plt.savefig(plot_path)
plt.close()

# Optional: display for your own check
# plt.show()
