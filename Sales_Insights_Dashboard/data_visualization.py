"""
data_visualization.py
---------------------
Generates charts from sales data.
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_revenue_by_region(df: pd.DataFrame, save_path: str):
    plt.figure(figsize=(6,4))
    plt.bar(df["Region"], df["Revenue"], color="skyblue")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_monthly_sales(df: pd.DataFrame, save_path: str):
    plt.figure(figsize=(6,4))
    plt.plot(df["Month"], df["Revenue"], marker="o", color="green")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
