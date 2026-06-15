import streamlit as st
import pandas as pd
import joblib
import os

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("About Project")

st.sidebar.info("""
Credit Card Fraud Detection using:

• Random Forest
• SMOTE
• Streamlit
• Power BI

Dataset:
284,807 transactions
492 fraud cases
""")

# ==========================
# LOAD MODEL
# ==========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "fraud_model.pkl"
)

model = joblib.load(model_path)

# ==========================
# TITLE
# ==========================
st.title("💳 Credit Card Fraud Detection Dashboard")

# ==========================
# TABS
# ==========================
tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "🔍 Fraud Prediction",
    "📈 Model Performance"
])

# ==========================
# TAB 1 - DASHBOARD
# ==========================
with tab1:

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", "284,807")
    col2.metric("Fraud Transactions", "492")
    col3.metric("Fraud %", "0.17%")

    st.info(
        "This dataset contains highly imbalanced credit card transactions with only 492 fraud cases."
    )

    st.subheader("Fraud vs Legitimate Transactions")

    fraud_data = pd.DataFrame(
        {"Count": [284315, 492]},
        index=["Legitimate", "Fraud"]
    )

    st.bar_chart(fraud_data)

    st.subheader("Project Insights")

    st.write("""
    • Only 0.17% of transactions are fraudulent.

    • The dataset is highly imbalanced.

    • SMOTE was used to balance the training data.

    • Random Forest achieved strong fraud detection performance.

    • ROC-AUC Score: 0.968
    """)

# ==========================
# TAB 2 - FRAUD PREDICTION
# ==========================
with tab2:

    st.header("Fraud Prediction")

    uploaded_file = st.file_uploader(
        "Upload Transaction CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        input_df = pd.read_csv(uploaded_file)

        # Remove target column if present
        if "Class" in input_df.columns:
            input_df = input_df.drop("Class", axis=1)

        st.subheader("Uploaded Data")
        st.dataframe(input_df.head())

        predictions = model.predict(input_df)

        fraud_count = int(sum(predictions))
        legit_count = int(len(predictions) - fraud_count)

        col1, col2 = st.columns(2)

        col1.metric("Legitimate Transactions", legit_count)
        col2.metric("Fraud Transactions", fraud_count)

        input_df["Prediction"] = predictions

        input_df["Prediction"] = input_df["Prediction"].map({
            0: "Legitimate",
            1: "Fraud"
        })

        st.subheader("Prediction Distribution")
        st.bar_chart(input_df["Prediction"].value_counts())

        st.subheader("Prediction Results")
        st.dataframe(input_df)

        csv = input_df.to_csv(index=False)

        st.download_button(
            label="📥 Download Results",
            data=csv,
            file_name="prediction_results.csv",
            mime="text/csv"
        )

# ==========================
# TAB 3 - MODEL PERFORMANCE
# ==========================
with tab3:

    st.header("Model Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ROC-AUC Score", "0.968")
        st.metric("Precision", "0.87")

    with col2:
        st.metric("Recall", "0.83")
        st.metric("F1 Score", "0.85")

    st.success(
        "Random Forest model trained using SMOTE-balanced data achieved strong fraud detection performance."
    )

    st.subheader("Classification Results")

    st.code("""
Precision : 0.87
Recall    : 0.83
F1-Score  : 0.85
ROC-AUC   : 0.968
""")

    st.subheader("Project Summary")

    st.write("""
    - Dataset Size: 284,807 transactions
    - Fraud Cases: 492
    - Algorithm: Random Forest Classifier
    - Imbalance Handling: SMOTE
    - Precision: 0.87
    - Recall: 0.83
    - F1 Score: 0.85
    - ROC-AUC Score: 0.968
    """)