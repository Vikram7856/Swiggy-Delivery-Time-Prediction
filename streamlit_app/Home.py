import streamlit as st
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def show_home():
    # Load dataset
    with open("swiggy_imputed_data.pkl", "rb") as file:
        df = pickle.load(file)

    # Title
    st.title("Delivery Time Prediction Platform")

    # Dataset preview
    st.subheader("📊 Sample of the Dataset:")
    st.dataframe(df.head())

    # Dataset dimensions
    rows, cols = df.shape

    # Introductory Section
    st.markdown(f"""
    Welcome to the **Delivery Time Prediction Site** — a data-driven web application designed to improve last-mile logistics by 
    accurately estimating food delivery times.

    This platform is powered by real-world Swiggy delivery data, enriched with custom preprocessing and machine learning techniques.

    **Dataset Summary**:
    - Records: **{rows:,}**
    - Features: **{cols}**
    - Includes information on:
        - 📦 **Order context**: `type_of_order`, `order_time_of_day`, `distance`, `ratings`
        - 🌦️ **Environment**: `weather`, `traffic`, `festival`, `city_type`, `is_weekend`
        - 🛵 **Logistics**: `type_of_vehicle`, `vehicle_condition`, `multiple_deliveries`, `pickup_time`

    The goal is to allow users to interactively input delivery parameters and receive intelligent **time predictions** based on trained machine learning models.
    """)

    # Tech stack
    st.markdown("""
    **Tech Stack**:
    - **Python**, **Scikit-learn**, **Pandas**, **MLflow**, **Optuna**
    - **Streamlit** for web app interface
    - **Custom Pipelines** for imputation, encoding, and scaling
    - Models and transformers saved via **Pickle**
    """)

    # Sidebar navigation prompt
    st.markdown("""
    👈 Use the sidebar to:
    - Input new delivery scenarios
    - View prediction outputs
    - Explore data visualizations
    """)

    # KDE + Histogram for 'time_taken'


    if 'time_taken' in df.columns:
      st.subheader("Delivery Time Distribution")

      fig, ax = plt.subplots(figsize=(12, 8))
      sns.histplot(df['time_taken'], bins=30, kde=True, edgecolor='black', ax=ax, line_kws={'color': 'red', 'linewidth': 2})

      ax.set_xlabel("Delivery Time (minutes)")
      ax.set_ylabel("Density / Frequency")
      ax.set_title("Histogram + KDE of Delivery Time")

      st.pyplot(fig)


    # Useful Links
    st.markdown("---")
    st.markdown("### 🔗 Useful Links")
    st.markdown("""
       - 📂 [GitHub Repository](https://github.com/Vikram7856/Swiggy-Delivery-Time-Prediction)
       - 📊 [DAGsHub Project Dashboard](https://dagshub.com/vkyadav7635/Swiggy-Delivery-Time-Prediction.mlflow)
       """)
