import numpy as np
import matplotlib.pyplot as plt

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
sales = np.array([200, 220, 250, 270, 300, 310, 330, 360, 390, 420, 450, 480])

plt.scatter(months, sales, color='blue', label='Sales Data')
coefficients = np.polyfit(months, sales, 1)  # 1 means linear
slope, intercept = coefficients

best_fit_line = slope * months + intercept

plt.plot(months, best_fit_line, color='red', label='Best Fit Line')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales with Best Fit Line')
plt.legend()
plt.show()