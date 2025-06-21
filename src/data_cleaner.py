# Handle missing data (fill/drop)
#
# Convert data types if necessary
#
# Remove duplicates
#
# Basic sanity checks (non-negative prices, etc.)

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)  # Length before cleaning

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') # Normalize 'Date' column to datetime format
    df = df.drop_duplicates(inplace=False) # Remove duplicates
    df = df.dropna(subset=['Close'])  # Drop rows where 'Close' is NaN
    df = df[df['Close'] > 0]  # Remove rows with negative or zero values in 'Close'
    df['Volume'] = df['Volume'].fillna(0).astype(int) # Handle missing 'Volume' (fill with 0 if NaN, convert to int)

    after = len(df)  # Length after cleaning
    print(f"Before: {before}, After: {after}, Removed: {before - after} duplicates.")

    return df

