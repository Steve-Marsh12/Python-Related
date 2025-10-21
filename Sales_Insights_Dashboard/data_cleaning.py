"""
data_cleaning.py
----------------
This module handles data loading and cleaning.
"""

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Loads CSV data into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath, parse_dates=["Date"])
        return df
    except Exception as e:
        raise FileNotFoundError(f"Error loading file {filepath}: {e}")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw sales data:
    - Removes missing values
    - Creates a 'Revenue' column
    - Ensures correct data types
    """
    df = df.dropna()
    df["Revenue"] = df["Units Sold"] * df["Unit Price"]
    df["Region"] = df["Region"].astype(str)
    df["Product"] = df["Product"].astype(str)
    return df
