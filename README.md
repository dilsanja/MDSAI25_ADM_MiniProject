
# 🎓 Back-to-School Buying Behavior – Mini Data Mining Project

A complete data pipeline project for analyzing and mining retail product data using clustering and association rule mining techniques.

---

## 📦 Project Structure

```
Back_to_School_MiniProject_GitRepo/
├── main.py                     # Entry point to run full pipeline
├── requirements.txt            # Required Python packages
├── README.md                   # Project description and guide
├── run_pipeline.ipynb          # Jupyter notebook for testing/visuals
├── notebooks/
│   └── run_pipeline.ipynb      # Jupyter notebook for testing/visuals
└── src/
    ├── clean_data.py           # Data cleaning functions
    ├── clustering.py           # K-means or other clustering methods
    ├── exploratory_analysis.py # Visualizations and summaries
    └── rule_mining.py          # Association rule mining (e.g. Apriori)
```

---

## 🚀 How to Run This Project

### ✅ 1. Install Requirements
```bash
pip install -r requirements.txt
```

### ✅ 2. Run the Full Pipeline
```bash
python main.py
```

This will:
- Clean the input dataset
- Perform clustering on product data
- Generate basic EDA (exploratory data analysis)
- Apply association rule mining to find product relationships

---

## 🧪 Testing (Optional)

You can test the pipeline step-by-step using the notebook:
```
run_pipeline.ipynb
```

---

## 📊 Data Used
- `OnlineRetail.xlsx` from UCI ML Repository (cleaned version)
- Derived CSV files and plots stored in the `data/` folder

---

## 🔧 Technologies Used
- Python 3.x
- pandas, numpy
- scikit-learn
- matplotlib / seaborn
- mlxtend (for association rules)

---

## ✍️ Author
P D S Perera (258733L)

---

## 📌 License
This project is for educational use only.
