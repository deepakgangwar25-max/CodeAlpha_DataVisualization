import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set visual theme
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.sans-serif": "DejaVu Sans", "font.size": 11})

# 1. Dataset Setup (Simulated retail performance dataset)
np.random.seed(42)
n_records = 300

categories = ["Technology", "Furniture", "Office Supplies"]
regions = ["North", "South", "East", "West"]

data = {
    "Order_ID": [f"ORD-{1000 + i}" for i in range(n_records)],
    "Region": np.random.choice(regions, n_records),
    "Category": np.random.choice(categories, n_records, p=[0.3, 0.3, 0.4]),
    "Sales": np.round(np.random.exponential(scale=250, size=n_records) + 20, 2),
    "Discount": np.random.choice([0.0, 0.1, 0.2, 0.3, 0.5], n_records),
}

df = pd.DataFrame(data)
# Profit calculation with discount penalty
df["Profit"] = np.round(
    df["Sales"] * (0.35 - df["Discount"])
    + np.random.normal(0, 15, size=n_records),
    2,
)

# 2. Multi-Panel Visual Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    "CodeAlpha Task 3: Comprehensive Sales & Profitability Dashboard",
    fontsize=18,
    fontweight="bold",
    y=0.98,
)

# Plot 1: Total Sales by Category (Bar Chart)
category_sales = (
    df.groupby("Category")["Sales"].sum().reset_index().sort_values(by="Sales")
)
sns.barplot(
    data=category_sales,
    x="Sales",
    y="Category",
    palette="Blues_d",
    ax=axes[0, 0],
)
axes[0, 0].set_title(
    "Total Sales Revenue by Category", fontsize=13, fontweight="semibold"
)
axes[0, 0].set_xlabel("Total Sales ($)")
axes[0, 0].set_ylabel("Category")

# Plot 2: Profit Distribution Across Regions (Box Plot)
sns.boxplot(
    data=df,
    x="Region",
    y="Profit",
    palette="Set2",
    boxprops=dict(alpha=0.8),
    ax=axes[0, 1],
)
axes[0, 1].axhline(0, color="red", linestyle="--", linewidth=1)
axes[0, 1].set_title(
    "Profit Distribution & Outliers by Region", fontsize=13, fontweight="semibold"
)
axes[0, 1].set_xlabel("Region")
axes[0, 1].set_ylabel("Profit ($)")

# Plot 3: Sales vs Profit with Discount Impact (Scatter Plot)
scatter = sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    size="Discount",
    sizes=(30, 200),
    palette="tab10",
    alpha=0.85,
    ax=axes[1, 0],
)
axes[1, 0].axhline(0, color="gray", linestyle=":", linewidth=1)
axes[1, 0].set_title(
    "Sales vs. Profitability (Sized by Discount)",
    fontsize=13,
    fontweight="semibold",
)
axes[1, 0].set_xlabel("Sales ($)")
axes[1, 0].set_ylabel("Profit ($)")
axes[1, 0].legend(loc="upper left", bbox_to_anchor=(1, 1))

# Plot 4: Average Discount vs Profit Heatmap
pivot_table = df.pivot_table(
    index="Category", columns="Region", values="Profit", aggfunc="mean"
)
sns.heatmap(
    pivot_table,
    annot=True,
    fmt=".1f",
    cmap="vlag",
    center=0,
    cbar_kws={"label": "Avg Profit ($)"},
    ax=axes[1, 1],
)
axes[1, 1].set_title(
    "Average Profit Heatmap: Category vs Region",
    fontsize=13,
    fontweight="semibold",
)
axes[1, 1].set_xlabel("Region")
axes[1, 1].set_ylabel("Category")

plt.tight_layout()
plt.savefig("task3_sales_dashboard.png", dpi=300)
plt.show()
