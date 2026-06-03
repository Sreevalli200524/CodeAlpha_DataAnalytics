import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# LOAD DATASET

df = pd.read_excel("Professional_Books_Dataset.xlsx")

# PREPARE DATA

rating_counts = df["Rating"].value_counts().sort_index()

price_counts = df["Price Category"].value_counts()

avg_price_by_rating = (
    df.groupby("Rating")["Price (£)"]
    .mean()
    .reset_index()
)

stock_counts = df["Stock Status"].value_counts()

# CREATE DASHBOARD

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Book Rating Distribution",
        "Price Category Distribution",
        "Average Price by Rating",
        "Stock Availability"
    ),
    specs=[
        [{"type": "bar"}, {"type": "pie"}],
        [{"type": "scatter"}, {"type": "bar"}]
    ]
)

# CHART 1 — Rating Distribution

fig.add_trace(
    go.Bar(
        x=rating_counts.index,
        y=rating_counts.values,
        name="Ratings"
    ),
    row=1,
    col=1
)

# CHART 2 — Price Categories

fig.add_trace(
    go.Pie(
        labels=price_counts.index,
        values=price_counts.values,
        hole=0.4
    ),
    row=1,
    col=2
)

# CHART 3 — Avg Price by Rating

fig.add_trace(
    go.Scatter(
        x=avg_price_by_rating["Rating"],
        y=avg_price_by_rating["Price (£)"],
        mode="lines+markers",
        name="Average Price"
    ),
    row=2,
    col=1
)

# CHART 4 — Stock Status

fig.add_trace(
    go.Bar(
        x=stock_counts.index,
        y=stock_counts.values,
        name="Stock"
    ),
    row=2,
    col=2
)

# DASHBOARD DESIGN

fig.update_layout(
    title={
        'text': "Interactive E-Commerce Analytics Dashboard",
        'x': 0.5,
        'xanchor': 'center'
    },

    template="plotly_dark",

    height=800,
    width=1200,

    showlegend=False
)

# SAVE DASHBOARD

fig.write_html("Interactive_Dashboard.html")

# SHOW DASHBOARD

fig.show()

print("\nINTERACTIVE DASHBOARD CREATED!")
print("Saved as: Interactive_Dashboard.html")