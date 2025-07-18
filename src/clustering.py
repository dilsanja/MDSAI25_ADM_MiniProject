import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/school_products_only.csv", parse_dates=['InvoiceDate'])

# Aggregate monthly quantity per product
product_monthly = df.groupby(['Description', df['InvoiceDate'].dt.to_period('M')])['Quantity'].sum().unstack().fillna(0)

# Normalize data
scaler = StandardScaler()
product_monthly_scaled = scaler.fit_transform(product_monthly)

# Apply KMeans Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(product_monthly_scaled)

# Add cluster labels to dataframe
product_monthly['Cluster'] = clusters
product_monthly.to_csv("data/clustered_product_trends.csv")

# Plot average trend per cluster
product_monthly.index = product_monthly.index.astype(str)
cluster_avg = product_monthly.groupby('Cluster').mean().T
cluster_avg.index = cluster_avg.index.astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(data=cluster_avg)
plt.title("Average Monthly Sales Trend per Cluster")
plt.xlabel("Month")
plt.ylabel("Average Quantity Sold (Standardized)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/clustered_trend_plot.png")
plt.close()

print("Clustering complete: results saved to data/")

# Add this function to integrate with main.py
def run():
    print(" Clustering logic ran from main.py")