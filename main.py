import pandas as pd

# Load the data
df = pd.read_csv('data/AAPL.csv', index_col='Date', parse_dates=True)

# Show the first few rows
print(df.head())
