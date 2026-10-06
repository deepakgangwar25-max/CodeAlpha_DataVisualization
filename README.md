# CodeAlpha Data Analytics Internship - Task 3: Data Visualization

## Overview
This project fulfills **Task 3: Data Visualization** of the CodeAlpha Data Analytics Internship. The goal is to transform raw retail sales data into intuitive, actionable charts and dashboards that uncover business insights and support strategic decision-making.

---

## Visualizations Included
The script generates a comprehensive 2x2 multi-panel dashboard (`task3_sales_dashboard.png`) containing:
1. **Total Sales Revenue by Category (Bar Chart):** Compares revenue contributions across Technology, Furniture, and Office Supplies.
2. **Profit Distribution & Outliers by Region (Box Plot):** Analyzes profitability spread and highlights high/low margin variances across North, South, East, and West territories.
3. **Sales vs. Profitability with Discount Impact (Scatter Plot):** Correlates gross transaction size with net profit while visually encoding discount rates.
4. **Average Profit Heatmap (Category vs. Region):** Identifies regional strengths and underperforming product lines at a glance.

---

## Key Insights
* **Revenue Leadership:** Technology yields the highest overall revenue, while Office Supplies maintains stable transaction volume with lower margin risk.
* **Discount Vulnerability:** Transactions with discount rates exceeding 30% heavily skew toward negative margins, pinpointing aggressive discounting as the primary source of losses.
* **Regional Variation:** The West and South regions show stronger outlier profits, whereas specific category segments in the East operate near break-even.

---

## Tech Stack
* **Python**
* **Pandas** & **NumPy** for data processing
* **Matplotlib** & **Seaborn** for chart styling and visualization

---

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/CodeAlpha_DataVisualization.git
   cd CodeAlpha_DataVisualization
