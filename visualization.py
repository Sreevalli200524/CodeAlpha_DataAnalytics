import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Professional_Books_Dataset.xlsx")

# Create dashboard layout
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 1. Rating Distribution

rating_counts = df["Rating"].value_counts().sort_index()

axs[0, 0].bar(
    rating_counts.index,
    rating_counts.values
)

axs[0, 0].set_title("Book Rating Distribution")
axs[0, 0].set_xlabel("Ratings")
axs[0, 0].set_ylabel("Number of Books")
axs[0, 0].grid(True)

# 2. Price Category Distribution

price_counts = df["Price Category"].value_counts()

axs[0, 1].pie(
    price_counts.values,
    labels=price_counts.index,
    autopct='%1.1f%%'
)

axs[0, 1].set_title("Price Category Distribution")

# 3. Average Price by Rating

avg_price = df.groupby("Rating")["Price (£)"].mean()

axs[1, 0].plot(
    avg_price.index,
    avg_price.values,
    marker='o'
)

axs[1, 0].set_title("Average Price by Rating")
axs[1, 0].set_xlabel("Rating")
axs[1, 0].set_ylabel("Average Price (£)")
axs[1, 0].grid(True)

# 4. Stock Availability

stock_counts = df["Stock Status"].value_counts()

axs[1, 1].bar(
    stock_counts.index,
    stock_counts.values
)

axs[1, 1].set_title("Stock Availability")
axs[1, 1].set_xlabel("Status")
axs[1, 1].set_ylabel("Count")
axs[1, 1].grid(True)

# Dashboard title
fig.suptitle(
    "E-Commerce Books Analytics Dashboard",
    fontsize=16
)

# Adjust layout
plt.tight_layout()

# Save dashboard
plt.savefig("Books_Analytics_Dashboard.png")

# Show dashboard
plt.show()

print("Dashboard created successfully!")