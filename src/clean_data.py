import pandas as pd
import os
# P D S Perera (Index : 258733L)

# Load data (ensure the Excel file is in the /data directory)
input_file = "data/OnlineRetail.xlsx"
output_file = "data/cleaned_retail.csv"
school_output_file = "data/school_products_only.csv"

if not os.path.exists(input_file):
    raise FileNotFoundError("Dataset not found. Please place 'OnlineRetail.xlsx' in the data/ directory.")

# Load and clean
df = pd.read_excel(input_file)
df.head();

# Drop missing values
df.dropna(subset=['CustomerID', 'Description'], inplace=True)

# Remove cancelled orders (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Remove non-positive Quantity or UnitPrice
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Parse InvoiceDate
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Day'] = df['InvoiceDate'].dt.day

# Create BasketID
df['BasketID'] = df['CustomerID'].astype(str) + '_' + df['InvoiceNo'].astype(str)

# Create Term Start Flag
school_months = [1, 8, 9]  # Jan, Aug, Sep
df['Is_Term_Start'] = df['Month'].isin(school_months).astype(int)

df['Description'] = df['Description'].astype(str).str.lower()
school_keywords = [
    "pen", "pencil", "ruler", "notebook", "book", "folder", "binder", "file", "highlighter",
    "marker", "crayon", "sharpener", "eraser", "glue", "scissors", "compass", "protractor",
    "school bag", "backpack", "whiteboard", "chalk", "tape", "sticky note", "index card",
    "stationery", "paper", "exercise book", "drawing pad", "calculator", "geometry box",
    "label", "pouch", "correction", "refill", "project paper", "stapler", "clip", "notepad",
    "sketch pad", "pencil case", "school uniform", "lunch box", "water bottle"
]
df['is_school_product'] = df['Description'].str.contains('|'.join(school_keywords))
df.to_csv(output_file, index=False)
df[df['is_school_product']].to_csv(school_output_file, index=False)
print(f"Saved: {output_file}, School products: {school_output_file}")

# Output cleaned file
#df.to_csv(output_file, index=False)
#print(f"Cleaned dataset saved to {output_file}")

# Add this function to integrate with main.py
def run():
    print(" Cleaning Data ran from main.py")
