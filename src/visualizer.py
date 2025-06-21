# Plot price over time
#
# Plot moving averages
#
# Plot daily returns histogram

import matplotlib.pyplot as plt
import pandas as pd


def plot_price(df, title="Stock Price Over Time"):
    plt.figure(figsize=(10,6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_moving_averages(df, windows=None):
    if windows is None:
        windows = [20, 50]
    plt.figure(figsize=(10,6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    for window in windows:
        ma = df['Close'].rolling(window=window).mean()
        plt.plot(df['Date'], ma, label=f'MA {window} days') # MA - Moving Average
    plt.legend()
    plt.title('Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

def plot_daily_returns_histogram(df: pd.DataFrame):
    """
    Plot a histogram of the daily returns of the stock.
    """
    if 'Daily Return' not in df.columns:
        df['Daily Return'] = df['Close'].pct_change()

    # Plot the histogram
    df['Daily Return'].hist(bins=50)
    plt.title("Histogram of Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.show()