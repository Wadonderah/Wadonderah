import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch real-time index data using yfinance from CNBC
nasdaq_data = yf.download('^IXIC', start='2024-02-29', end='2024-03-01', interval='30m')
us30_data = yf.download('^DJI', start='2024-02-29', end='2024-03-01', interval='30m')

# Calculate moving averages
nasdaq_data['Short_MA'] = nasdaq_data['Close'].rolling(window=10).mean()
nasdaq_data['Long_MA'] = nasdaq_data['Close'].rolling(window=30).mean()
us30_data['Short_MA'] = us30_data['Close'].rolling(window=10).mean()
us30_data['Long_MA'] = us30_data['Close'].rolling(window=30).mean()

# Identify supply and demand zones (example criteria)
nasdaq_supply_zone = nasdaq_data['Close'] > nasdaq_data['Long_MA']
us30_supply_zone = us30_data['Close'] > us30_data['Long_MA']

# Plot the data and zones
plt.figure(figsize=(10, 6))
plt.plot(nasdaq_data.index, nasdaq_data['Close'], label='Nasdaq (US100)')
plt.plot(us30_data.index, us30_data['Close'], label='US30 (Dow Jones)')
plt.plot(nasdaq_data.index, nasdaq_data['Short_MA'], label='Short MA', linestyle='--')
plt.plot(us30_data.index, us30_data['Short_MA'], label='Short MA', linestyle='--')
plt.fill_between(nasdaq_data.index, nasdaq_data['Close'], where=nasdaq_supply_zone, color='red', alpha=0.2, label='Nasdaq Supply Zone')
plt.fill_between(us30_data.index, us30_data['Close'], where=us30_supply_zone, color='green', alpha=0.2, label='US30 Supply Zone')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Supply and Demand Zones for Nasdaq and US30 (Real-Time Data from CNBC)')
plt.legend()
plt.grid(True)
plt.show()
