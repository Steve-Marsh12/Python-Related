"""
main.py
-------
Main script to run the Sales Insights Dashboard project.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

from data_cleaning import load_data, clean_data
from data_analysis import total_revenue, revenue_by_region, top_products, monthly_sales
from data_visualization import plot_revenue_by_region, plot_monthly_sales

# Define paths
DATA_PATH = os.path.join("data", "raw_sales.csv")
REPORT_PATH = os.path.join("reports", "sales_summary.pdf")
REGION_PLOT = os.path.join("reports", "revenue_by_region.png")
MONTHLY_PLOT = os.path.join("reports", "monthly_sales.png")

def generate_report():
    """
    Generates a PDF report with sales insights and charts.
    """
    # Load and clean
    df = load_data(DATA_PATH)
    df = clean_data(df)

    # Analysis
    total = total_revenue(df)
    region_rev = revenue_by_region(df)
    top_prods = top_products(df)
    monthly_rev = monthly_sales(df)

    # Visualizations
    plot_revenue_by_region(region_rev, REGION_PLOT)
    plot_monthly_sales(monthly_rev, MONTHLY_PLOT)

    # Build PDF
    doc = SimpleDocTemplate(REPORT_PATH, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Sales Insights Report</b>", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Total Revenue: £{total:,.2f}", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Top Products</b>", styles["Heading2"]))
    for _, row in top_prods.iterrows():
        story.append(Paragraph(f"{row['Product']}: £{row['Revenue']:,.2f}", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Revenue by Region</b>", styles["Heading2"]))
    story.append(Image(REGION_PLOT, width=400, height=200))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Monthly Sales Trend</b>", styles["Heading2"]))
    story.append(Image(MONTHLY_PLOT, width=400, height=200))

    doc.build(story)
    print(f"Report generated: {REPORT_PATH}")

if __name__ == "__main__":
    generate_report()
