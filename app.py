# -*- coding: utf-8 -*-
"""
Rainfall Prediction Web App
Final Polished Version for Deployment
"""

import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Rainfall Prediction",
    page_icon="🌧️",
    layout="centered",
)

# ------------------------------
# Custom CSS Styling
# ------------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #0E1117;
        }
        .prediction-card {
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            animation: fadeIn 1.5s;
        }
        .rain {
            background-color: #E6F2FF;
            border: 2px solid #1E90FF;
            color: #1E90FF;
        }
        .norain {
            background-color: #FFF9E6;
            border: 2px solid #FFD700;
            color: #FFD700;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# Load Model
# ------------------------------
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

# ------------------------------
# Prediction Function
# ------------------------------
def rainfall_prediction(input_data):
    input_df = pd.DataFrame([input_data], columns=feature_names)
    prediction = model.predict(input_df)
    return 1 if prediction[0] == 1 else 0


# ------------------------------
# Main App
# ------------------------------
def main():
    # Title
    st.markdown(
        """
        <h1 style="text-align:center; color:#00BFFF; font-size:40px;">
            🌦️ Rainfall Prediction using Machine Learning 🌦️
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center; font-size:18px; color:lightgrey;'>"
        "Enter the weather parameters below to predict whether rainfall will occur."
        "</p>",
        unsafe_allow_html=True,
    )

    # Two-column layout
    col1, col2 = st.columns(2)

    with col1:
        pressure = st.number_input("🌡️ Pressure Level (hPa)", min_value=900.0, max_value=1100.0, step=0.1)
        maxtemp = st.number_input("🔥 Maximum Temperature (°C)", min_value=-10.0, max_value=60.0, step=0.1)
        humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100, step=1)
        cloud = st.number_input("☁️ Cloud Coverage (%)", min_value=0, max_value=100, step=1)

    with col2:
        rainfall = st.number_input("🌧️ Rainfall Measurement (mm)", min_value=0.0, max_value=500.0, step=0.1)
        sunshine = st.number_input("☀️ Sunshine Duration (hours)", min_value=0.0, max_value=24.0, step=0.1)
        windspeed = st.number_input("🌬️ Wind Speed (km/h)", min_value=0.0, max_value=200.0, step=0.1)

    st.markdown("---")

    # Prediction button
    if st.button("🔮 Predict Rainfall", use_container_width=True):
        prediction = rainfall_prediction([pressure, maxtemp, humidity, cloud, rainfall, sunshine, windspeed])

        # Fancy Result Card
        if prediction == 1:
            st.markdown(
                "<div class='prediction-card rain'>🌧️ Yes, Rainfall is likely! 🌧️</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='prediction-card norain'>☀️ No Rainfall Expected! ☀️</div>",
                unsafe_allow_html=True,
            )

    # ------------------------------
    # Footer Options
    # ------------------------------
    st.markdown("---")
    st.subheader("📜 Menu")

    option = st.selectbox(
        "Choose an option:",
        ["About", "Developer", "Contact", "Version", "Features", "Help", "More"]
    )

    if option == "About":
        st.info("🌦️ This app predicts rainfall based on weather parameters like humidity, temperature, pressure, windspeed, etc.")
    elif option == "Developer":
        st.info("👨‍💻 Developed by Ayush Raj")
    elif option == "Contact":
        st.info("📧: rajaayushwow0@email.com | 🌐: https://ayussh-portfolio.vercel.app/ ")
    elif option == "Version":
        st.info("🛠️ Version 1.0.0")
    elif option == "Features":
        st.success(
            "- Accurate Rainfall Prediction\n"
            "- Interactive Charts\n"
            "- User-friendly Interface\n"
            "- Insights for Better Understanding\n"
            "- Lightweight and Fast"
        )
    elif option == "Help":
        st.warning("ℹ️ For help, please refer to the documentation or contact support.")
    elif option == "More":
        st.info("✨ More exciting features coming soon! Stay tuned.")

    # ------------------------------
    # Footer Text
    # ------------------------------
    st.markdown(
        "<br><hr><p style='text-align:center; color:grey;'>"
        "Developed by <b>Ayush Raj</b> with ❤️ using Streamlit | Powered by Machine Learning"
        "</p>",
        unsafe_allow_html=True,
    )


# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    main()
