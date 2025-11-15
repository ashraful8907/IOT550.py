import pandas as pd
import matplotlib.pyplot as plt

# Read CSV with comma as separator
df = pd.read_csv(r"nasdaq\HistoricalData_AAPL.csv", sep=",")

# Clean columns
df.columns = df.columns.str.strip().str.replace('\ufeff', '')

# Convert 'Close' column to numeric (remove $)
df['Close'] = df['Close'].replace('[\$,]', '', regex=True).astype(float)

# Convert 'Date' to datetime and sort
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], color='skyblue', marker='o')
plt.title("Apple Stock Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
