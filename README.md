
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
├── data/
│   └── OnlineRetail.xlsx       # Row Data
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

## 📂 Dataset Setup

The dataset used in this project is derived from the UCI Online Retail dataset and filtered for school-related products.

To run the project:

1. **Create a `data/` folder** in the root directory (if it doesn't exist).
2. **Download the dataset file** from the link below.
3. **Place it inside the `data/` folder.**

📥 [Download OnlineRetail.xlsx](https://drive.google.com/uc?export=download&id=1kMjkYglN64xDCjsPw1lZ0fZBYDQ9bVHx)



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

### 🔗 Live Dashboard Link

[![View Dashboard](https://img.shields.io/badge/Click_to_View-Looker_Studio-blue?style=for-the-badge&logo=google)](https://lookerstudio.google.com/reporting/f32c7d09-f2cf-45f3-8bd4-fd0fce87b74e)

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
