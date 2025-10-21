"""
data_analysis.py
----------------
This module provides analysis functions for sales data.
"""

import pandas as pd

def total_revenue(df: pd.DataFrame) -> float:
    """Returns total revenue across all sales."""
    return df["Revenue"].sum()

def revenue_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Returns revenue grouped by region."""
    return df.groupby("Region")["Revenue"].sum().reset_index()

def top_products(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Returns top N products by total revenue."""
    return df.groupby("Product")["Revenue"].sum().reset_index().nlargest(n, "Revenue")

def monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Returns total revenue per month."""
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    return df.groupby("Month")["Revenue"].sum().reset_index()
