# 🇮🇳 India Exports Analytics & ML Dashboard

An end-to-end **Data Analysis + Machine Learning + Deployment** project that analyzes India's export data (2017–2023) and provides interactive insights with predictive modeling.

🚀 **Live App:** [https://india-exports-data-analysis-p37zhzsxupy28yuxjb4utz.streamlit.app/](https://india-exports-data-analysis-p37zhzsxupy28yuxjb4utz.streamlit.app/)
📂 **GitHub Repo:** [https://github.com/PrajwalKhambad/India-Exports-Data-Analysis-Project](https://github.com/PrajwalKhambad/India-Exports-Data-Analysis-Project)

---

## 📊 Features

### 🔹 Exploratory Data Analysis

* Export value overview
* Country-wise analysis
* Commodity-wise analysis
* Yearly trends

### 🔹 Comparative Insights

* Physical vs Non-Physical exports
* Export composition over time

### 🔹 Machine Learning

* Regression → Physical exports value prediction
* Classification → Service export tier prediction

---

# ⚙️ Data Processing & Design Decisions

### Handling Missing Quantities (Key Challenge)

The raw dataset contained **many missing values in the `Quantity` column**.

This created two fundamentally different types of exports:

### 1️⃣ Physical Exports (Goods)

* Have Quantity + Unit
* Examples: Steel, Rice, Machinery, Chemicals
* Measurable in physical units
* Suitable for **regression modeling**

### 2️⃣ Non-Physical Exports (Services/Intangibles)

* No Quantity/Unit
* Examples: Software services, Consulting, Royalties
* Value-only data
* Highly volatile & demand-driven
* Better suited for **classification instead of regression**

### Solution Implemented

The dataset was split into:

* `df_with_qty` → Physical exports
* `df_without_qty_strict` → Non-physical exports

Separate ML models were trained for each type to ensure:

* Better accuracy
* Domain correctness
* More realistic predictions

This avoids mixing incompatible data and significantly improves modeling quality.

---

## 🧠 ML Approach

### Physical Exports → Regression

Model: CatBoost Regressor
Features:

* Year
* Country
* Commodity
* Quantity

Metrics:

* RMSE
* R²

---

### Non-Physical Exports → Classification

Model: CatBoost Classifier

Exports grouped into tiers:

* Low
* Medium
* High

Reason:
Exact value prediction is unreliable due to service volatility.
Tier-based classification provides more robust and interpretable results.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* CatBoost
* Scikit-learn
* NumPy

---

## 📂 Project Structure

```
app.py
requirements.txt
ml/
views/
modules/
data/
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deployment

Deployed using **Streamlit Community Cloud**

---

## 🎯 Key Learnings

* Real-world data cleaning
* Handling missing values intelligently
* Domain-aware modeling
* Regression vs Classification design choices
* Interactive dashboards
* Cloud deployment

---

## 👤 Author

Your Name
LinkedIn: [https://linkedin.com/in/Prajwal%20Khambad](https://linkedin.com/in/Prajwal%20Khambad)
GitHub: [https://github.com/PrajwalKhambad](https://github.com/PrajwalKhambad)
