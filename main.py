# main.py
# P D S Perera (Index : 258733L)
import subprocess
import sys
import os

if not os.path.exists("data/OnlineRetail.xlsx"):
    raise FileNotFoundError("Dataset not found. Please download it and place it in the 'data/' folder.")

# --- Step 1: Required Python packages ---
required_packages = [
    "pandas", "numpy", "matplotlib", "seaborn",
    "mlxtend", "scikit-learn", "openpyxl"
]

def install_packages(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"📦 Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install missing packages
install_packages(required_packages)

# --- Step 2: Run project pipeline modules ---
try:
    from src import clean_data, clustering, exploratory_analysis, rule_mining
except ImportError:
    print("❌ Failed to import one or more modules from 'src/'. Please check your file structure.")
    sys.exit(1)

def run_pipeline():
    print("🚿 Step 1: Cleaning Data")
    clean_data.run()

    print("🧠 Step 2: Running Clustering")
    clustering.run()

    print("📊 Step 3: Exploratory Data Analysis")
    exploratory_analysis.run()

    print("🔗 Step 4: Association Rule Mining")
    rule_mining.run()

    print("✅ All steps completed successfully!")

# Entry point
if __name__ == "__main__":
    run_pipeline()
