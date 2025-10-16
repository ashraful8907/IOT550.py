import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Slope and intercept
m = 2      # example slope
b = 5      # example intercept

# Number of data points
n_points = 50

X = np.linspace(0, 10, n_points)  # generates 50 evenly spaced points between 0 and 10

# Noise level (standard deviation)
noise = 3

# Generate Y values
Y = m * X + b + np.random.normal(0, noise, n_points)

# Create a DataFrame
data = pd.DataFrame({'X': X, 'Y': Y})

# Save to CSV
data.to_csv('synthetic_data.csv', index=False)

plt.scatter(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Synthetic Data with Noise')
plt.show()
