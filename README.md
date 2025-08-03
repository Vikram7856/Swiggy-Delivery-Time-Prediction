#  Swiggy Delivery Time Prediction

This project helps predict how long a food delivery might take, using real data from Swiggy orders.

It looks at things like the type of order, traffic, weather, and delivery vehicle etc, to make smart predictions using machine learning.

The goal is to make last-mile delivery faster and more accurate.

You can explore the code, check how the model works, and run the Streamlit app on your own computer to test different delivery situations.

---

##  Dataset Summary

- **Records:** 45,073
- **Features:** 19

### Includes Information On:
- 📦 **Order Context**: `type_of_order`, `order_time_of_day`, `distance`, `ratings`
- 🌦️ **Environment**: `weather`, `traffic`, `festival`, `city_type`, `is_weekend`
- 🛵 **Logistics**: `type_of_vehicle`, `vehicle_condition`, `multiple_deliveries`, `pickup_time`

---

##  Tech Stack

- **Languages & Libraries**: Python, Scikit-learn, Pandas
- **Web Framework**: Streamlit
- **Model Management**: MLflow, Optuna
- **Serialization**: Pickle
- **Custom Preprocessing Pipelines**:
  - Imputation
  - Encoding
  - Scaling

---

## 🔗 Useful Links

- 📊 [DAGsHub MLflow Dashboard](https://dagshub.com/vkyadav7635/Swiggy-Delivery-Time-Prediction.mlflow)
- 🗂️ [Google Drive (Data & Artifacts)](https://drive.google.com/drive/folders/1amTEFs91NO_icdShALPP7RNdAg5ZMk35)
---

  ## App Preview

Here are some screenshots of the Streamlit web application in action:

### Home Page

![Home Page 1](Streamlit_home_page-0001.jpg)
![Home Page 2](Streamlit_home_page-0002.jpg)
![Home Page 3](Streamlit_home_page-0003.jpg)

### App Pages

![App Page 1](Streamlit_app_page-0001.jpg)
![App Page 2](Streamlit_app_page-0002.jpg)
![App Page 3](Streamlit_app_page-0003.jpg)
![App Page 4](Streamlit_app_page-0004.jpg)

