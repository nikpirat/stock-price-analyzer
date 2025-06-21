# Load CSV or API data
#
# Return Pandas DataFrame

import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=['Date'])
    return df