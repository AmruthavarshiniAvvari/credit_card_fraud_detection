# 💳 Credit Card Fraud Detection System

## 📌 Overview
This project is a **Machine Learning-based Credit Card Fraud Detection System** built using Python and deployed using **Streamlit + GitHub integration**.

The system predicts whether a transaction is **fraudulent or legitimate** using trained ML models. It helps in identifying suspicious transactions and reducing financial fraud risks.

---

## 🚀 Live Deployment
👉 Streamlit App: https://creditcardfrauddetection-3aqpyvpvp857eg8j7uqwcu.streamlit.app/

---

## 📊 Dataset Information
- Dataset used: **Credit Card Fraud Detection Dataset (Kaggle)**
- Source: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Contains:
  - 284,807 transactions
  - 492 fraud cases (highly imbalanced dataset)
  - Features: V1–V28 (anonymized), Time, Amount, Class

⚠️ Note:
The dataset file (`creditcard.csv`) is **not uploaded to this repository** because of its large size. It can be downloaded directly from Kaggle using the link above.

---

## 🧠 Machine Learning Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- SMOTE
- XGBoost

### Evaluation Metrics:
- Accuracy Score
- Confusion Matrix
- Precision, Recall, F1-Score
- ROC-AUC Score

---

## ⚙️ Tech Stack
- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit (for web app)
- Git & GitHub (version control & deployment)

---

## 🔄 Project Workflow
1. Data Collection (Kaggle Dataset)
2. Data Preprocessing (scaling, cleaning, imbalance handling)
3. Exploratory Data Analysis (EDA)
4. Model Training & Selection
5. Model Evaluation
6. Streamlit Web App Development
7. Deployment using GitHub + Streamlit Cloud

---

## 🖥️ How to Run This Project Locally

```bash
# Clone repository
git clone https://github.com/your-username/credit_card_fraud_detection.git

# Move to project directory
cd credit_card_fraud_detection

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

---

## 📸 Screenshots

🏠 Dashboard Page
![Dashboard Page](screenshots/dashboard.png)
🔍 Prediction Page
![Prediction Page](screenshots/fraudprediction.png)
📊 Model Results
![Results](screenshots/modelperformance.png)

---

## 📈 Results

- Achieved high accuracy for legitimate transactions
- Focused on improving recall for fraud detection due to class imbalance
- Random Forest performed best among tested models
- Implement SMOTE for better imbalance handling

---

## 👩‍💻 Author

Amrutha varshini Avvari
Aspiring Data Scientist 🚀



# Run Streamlit app
streamlit run app.py
