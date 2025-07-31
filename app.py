# app.py

import streamlit as st
from Home import show_home
from Time_prediction import show_prediction

# Sidebar for navigation
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction"])

# Page router
if page == "Home":
    show_home()
elif page == "Prediction":
    show_prediction()
