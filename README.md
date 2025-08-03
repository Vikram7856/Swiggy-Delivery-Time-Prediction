# 🚀 Swiggy Delivery Time Prediction

Welcome to the **Delivery Time Prediction Site** — a data-driven web application designed to enhance last-mile logistics by accurately estimating food delivery times.

This platform leverages real-world Swiggy delivery data, enriched with custom preprocessing pipelines and advanced machine learning models.

---

## 📊 Dataset Summary

- **Records:** 45,073
- **Features:** 19

### Includes Information On:
- 📦 **Order Context**: `type_of_order`, `order_time_of_day`, `distance`, `ratings`
- 🌦️ **Environment**: `weather`, `traffic`, `festival`, `city_type`, `is_weekend`
- 🛵 **Logistics**: `type_of_vehicle`, `vehicle_condition`, `multiple_deliveries`, `pickup_time`

---

## 🎯 Project Goal

Allow users to **interactively input delivery parameters** and receive **intelligent time predictions** based on trained machine learning models.

---

## 🧠 Tech Stack

- **Languages & Libraries**: Python, Scikit-learn, Pandas
- **Web Framework**: Streamlit
- **Model Management**: MLflow, Optuna
- **Serialization**: Pickle
- **Custom Preprocessing Pipelines**:
  - Imputation
  - Encoding
  - Scaling

---

## 📌 Project Highlights

- Predict delivery time using ML models trained on preprocessed data
- Built with `scikit-learn`, `Streamlit`, `Optuna`, and `MLflow`
- Includes custom preprocessing pipelines: encoding, imputation, scaling
- Deployable interactive web app for real-time inputs and prediction
- Artifacts tracked with MLflow and available on DAGsHub
- Data & model files hosted on Google Drive for transparency and reproducibility

---

## 🔗 Useful Links

- 📊 [DAGsHub MLflow Dashboard](https://dagshub.com/vkyadav7635/Swiggy-Delivery-Time-Prediction.mlflow)
- 🗂️ [Google Drive (Data & Artifacts)](https://drive.google.com/drive/folders/1amTEFs91NO_icdShALPP7RNdAg5ZMk35)
