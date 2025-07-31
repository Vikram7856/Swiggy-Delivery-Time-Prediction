# prediction.py

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder, OneHotEncoder, FunctionTransformer, PowerTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from sklearn.compose import TransformedTargetRegressor

from lightgbm import LGBMRegressor
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

# ['age', 'ratings', 'weather', 'traffic', 'vehicle_condition',
#     'type_of_order', 'type_of_vehicle', 'multiple_deliveries', 'festival',
#      'city_type', 'time_taken', 'city_name', 'order_day', 'order_month',
#     'order_day_of_week', 'is_weekend', 'pickup_time', 'order_time_of_day',
#      'distance']



def show_prediction():
    with open("swiggy_imputed_data.pkl", "rb") as file:
        df = pickle.load(file)



    pipeline = joblib.load("full_pipeline.pkl")  # Save it after training with joblib.dump(...)

    st.header("Predict Delivery Time")
    st.title("Enter the delivery details:")
    st.subheader("🔘 Select Features")

    # 1. Numerical Inputs
    age = st.selectbox("Age", options=list(range(18, 61)))
    ratings = st.number_input("Ratings", min_value=1.0, max_value=5.0, step=0.1, format="%.1f")

    # 2. Categorical Inputs
    weather = st.selectbox("Weather", sorted(df["weather"].dropna().unique()))
    traffic = st.selectbox("Traffic", sorted(df["traffic"].dropna().unique()))

    # Vehicle Condition (custom labels)
    vehicle_condition_mapping = {
        "0 New Vehicle": 0,
        "1 Mid-Age Vehicle": 1,
        "2 Old Vehicle": 2
    }
    vehicle_label = st.selectbox("Vehicle Condition", list(vehicle_condition_mapping.keys()))
    vehicle_condition = vehicle_condition_mapping[vehicle_label]

    type_of_order = st.selectbox("Type of Order", sorted(df['type_of_order'].dropna().unique()))
    type_of_vehicle = st.selectbox("Type of Vehicle", sorted(df['type_of_vehicle'].dropna().unique()))

    # Multiple Deliveries
    multiple_deliveries_mapping = {
        "0 (Single delivery)": 0.0,
        "1 (One extra delivery)": 1.0,
        "2 (Two extra deliveries)": 2.0,
        "3 (Three extra deliveries)": 3.0
    }
    delivery_label = st.selectbox("Number of Multiple Deliveries:", list(multiple_deliveries_mapping.keys()))
    multiple_deliveries = multiple_deliveries_mapping[delivery_label]

    festival = st.selectbox("Festival", sorted(df['festival'].dropna().unique()))
    city_type = st.selectbox("City Type", sorted(df['city_type'].dropna().unique()))
    is_weekend_map = {
        "No (Weekday)": 0,
        "Yes (Weekend)": 1
    }
    weekend_label = st.selectbox("Is Weekend", list(is_weekend_map.keys()))
    is_weekend = is_weekend_map[weekend_label]

    # Corrected numerical inputs
    pickup_time_options = np.arange(4.0, 31.0, 1).tolist()
    pickup_time = st.selectbox("Pickup Time (Minutes)", pickup_time_options)

    order_time_of_day = st.selectbox("Order Time of Day", sorted(df['order_time_of_day'].dropna().unique()))

    # Corrected numerical inputs
    distance = st.number_input("Distance (km)", min_value=0.5, max_value=30.0, step=0.5)

    # Optional: Show collected input
    st.markdown("### 🧾 Summary of your inputs")
    st.json({
        "age": age,
        "ratings": ratings,
        "weather": weather,
        "traffic": traffic,
        "vehicle_condition": vehicle_condition,
        "type_of_order": type_of_order,
        "type_of_vehicle": type_of_vehicle,
        "multiple_deliveries": multiple_deliveries,
        "festival": festival,
        "city_type": city_type,
        "is_weekend": is_weekend,
        "pickup_time": pickup_time,
        "order_time_of_day": order_time_of_day,
        "distance": distance
    })

    # Predict button
    if st.button("Predict"):
        # Combine values into a DataFrame
        data = [[age, ratings, weather, traffic, vehicle_condition,
                 type_of_order, type_of_vehicle, multiple_deliveries, festival,
                 city_type, is_weekend, pickup_time, order_time_of_day, distance]]

        columns = ['age', 'ratings', 'weather', 'traffic', 'vehicle_condition',
                   'type_of_order', 'type_of_vehicle', 'multiple_deliveries', 'festival',
                   'city_type', 'is_weekend', 'pickup_time', 'order_time_of_day', 'distance']

        one_df = pd.DataFrame(data, columns=columns)
        st.write("✅ Input Preview:")
        st.dataframe(one_df)

        # Run prediction
        try:
            predicted_time = pipeline.predict(one_df)[0]
            st.success(f" Estimated Delivery Time: **{predicted_time:.2f} minutes**")
        except Exception as e:
            st.error(" Prediction failed. Please check your pipeline or inputs.")
            st.exception(e)
