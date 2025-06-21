# Calculate daily returns
#
# Calculate moving averages (e.g., 20-day, 50-day)
#
# Summary statistics (mean, std dev, volatility)

import pandas as pd
import numpy as np

def moving_average(df: pd.DataFrame, window: int) -> pd.Series:
    return df['Close'].rolling(window=window).mean()

def calculate_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the daily return based on the 'Close' price column.
    """
    df['Daily Return'] = df['Close'].pct_change()
    return df

def summary_stats(df: pd.DataFrame) -> dict:
    """
    Computes summary statistics including average daily return, volatility,
    and other relevant metrics based on the 'Daily Return' column.
    """
    if 'Daily Return' not in df.columns:
        raise ValueError("'Daily Return' column is missing. Please calculate it before using this function.")

    return {
        'mean': df['Daily Return'].mean(),
        'volatility': df['Daily Return'].std() * np.sqrt(252),  # annualized volatility
        'max': df['Daily Return'].max(),
        'min': df['Daily Return'].min(),
        'median': df['Daily Return'].median(),
        'total_return': (df['Daily Return'] + 1).prod() - 1  # Total return over the period
    }