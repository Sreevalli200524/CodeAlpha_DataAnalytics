import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random

# PAGE SETTINGS

st.set_page_config(
    page_title="Amazon Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# GENERATE DATA

products = [
    "Wireless Mouse",
    "Gaming Keyboard",
    "Laptop Stand",
    "Bluetooth Speaker",
    "USB Hub",
    "Smart Watch",
    "Phone Case",
    "LED Monitor",
    "Power Bank",
    "Mechanical Keyboard"
]

categories = [
    "Electronics",
    "Accessories",
    "Computer",
    "Audio",
    "Mobile"
]

data = []

for i in range(300):

    product = random.choice(products)

    category = random.choice(categories)

    rating = random.randint(1, 5)

    sales = random.randint(50, 500)

    revenue = sales * random.randint(20, 200)

    data.append([
        product,
        category,
        rating,
        sales,
        revenue
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Product",
        "Category",
        "Rating",
        "Sales",
        "Revenue"
    ]
)

# HEADER

st.title("🛒 Amazon Sales Analytics Dashboard")

st.markdown(
    "Interactive dashboard for product sales and revenue analysis."
)

st.divider()

# KPI SECTION

col1, col2, col3, col4 = st.columns(4)

col1.metric("Products", df["Product"].nunique())

col2.metric("Total Sales", int(df["Sales"].sum()))

col3.metric("Revenue", f"${int(df['Revenue'].sum()):,}")

col4.metric("Avg Rating", round(df["Rating"].mean(), 1))

st.divider()

# CATEGORY SALES DATA

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
)

# PRODUCT REVENUE DATA

product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
)

# RATING DATA

rating_counts = (
    df["Rating"]
    .value_counts()
    .sort_index()
)

# CREATE FIGURES MANUALLY

# BAR CHART

fig1 = go.Figure()

fig1.add_trace(
    go.Bar(
        x=category_sales.index.tolist(),
        y=category_sales.values.tolist(),
        marker_color="orange"
    )
)

fig1.update_layout(
    title="Category-wise Sales",
    height=400
)

# PIE CHART

fig2 = go.Figure()

fig2.add_trace(
    go.Pie(
        labels=product_revenue.index.tolist(),
        values=product_revenue.values.tolist(),
        hole=0.4
    )
)

fig2.update_layout(
    title="Revenue Contribution"
)

# HISTOGRAM STYLE BAR

fig3 = go.Figure()

fig3.add_trace(
    go.Bar(
        x=rating_counts.index.tolist(),
        y=rating_counts.values.tolist(),
        marker_color="green"
    )
)

fig3.update_layout(
    title="Customer Ratings Distribution",
    height=400
)

# TOP PRODUCTS REVENUE

top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig4 = go.Figure()

fig4.add_trace(
    go.Bar(
        x=top_products.index.tolist(),
        y=top_products.values.tolist(),

        marker_color=[
            "#FF6B6B",
            "#4ECDC4",
            "#FFD93D",
            "#6C5CE7",
            "#00CEC9",
            "#FDCB6E",
            "#E17055",
            "#0984E3",
            "#55EFC4",
            "#A29BFE"
        ]
    )
)

fig4.update_layout(
    title="Top Product Revenue",

    xaxis_title="Products",

    yaxis_title="Revenue",

    height=400
)

# DASHBOARD LAYOUT

left, right = st.columns(2)

with left:
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)

with right:
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig4, use_container_width=True)

# INSIGHTS

st.divider()

st.subheader("📈 Business Insights")

st.markdown("""
- Electronics products generate strong sales.
- Higher-rated products tend to produce more revenue.
- Revenue distribution is balanced across products.
- Customer ratings mostly fall between 3 and 5.
""")

# DATA PREVIEW

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(20))