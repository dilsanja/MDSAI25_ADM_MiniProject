import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load data
df = pd.read_csv("data/school_products_only.csv")

# Filter to only term-start period
df = df[df['Is_Term_Start'] == 1]

# Create basket-product matrix
grouped = df.groupby(['BasketID', 'Description'])['Quantity'].sum().unstack().fillna(0)
grouped = grouped.applymap(lambda x: 1 if x > 0 else 0)

# Apply Apriori Algorithm
frequent_itemsets = apriori(grouped, min_support=0.01, use_colnames=True)

# Generate Association Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Save to CSV
rules.to_csv("data/association_rules_term_start.csv", index=False)
print(f"Saved {len(rules)} rules to data/association_rules_term_start.csv")

def run():
    print(" Association Rule Mining ran from main.py")