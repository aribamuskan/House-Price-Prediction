import streamlit as st
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# Page title
st.title("🏠 House Price Prediction")

st.write("Enter the house details below to predict its price.")

# Input section
st.subheader("🏠 Enter House Details")

area = st.number_input(
    "Area (sqft)",
    min_value=500,
    max_value=10000,
    value=2000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

age = st.number_input(
    "House Age",
    min_value=0,
    max_value=100,
    value=10
)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([[area, bedrooms, bathrooms, age]])

    st.success(
        f"Estimated House Price: Rs. {prediction[0]:,.0f}"
    )