import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/school_products_only.csv", parse_dates=['InvoiceDate'])

# Set style
sns.set(style="whitegrid")

# 1. Monthly Sales Volume
monthly_sales = df.groupby(['Year', 'Month'])['Quantity'].sum().reset_index()
monthly_sales['Period'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales['Period'], monthly_sales['Quantity'], marker='o')
plt.title("Monthly Sales Volume")
plt.xlabel("Month")
plt.ylabel("Total Quantity Sold")
plt.tight_layout()
plt.savefig("data/monthly_sales_trend.png")
plt.close()

# 2. Top 10 Products During Term Start
term_df = df[df['Is_Term_Start'] == 1]
top_products = term_df.groupby('Description')['Quantity'].sum().nlargest(10).sort_values()

plt.figure(figsize=(8, 6))
top_products.plot(kind='barh', color='steelblue')
plt.title("Top 10 Products During Term Start")
plt.xlabel("Quantity Sold")
plt.tight_layout()
plt.savefig("data/top_term_start_products.png")
plt.close()

print("EDA complete: charts saved to data/")
def run():
    print(" Exploratory Data Analysis ran from main.py")