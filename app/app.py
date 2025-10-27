import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")

with st.form("predict"):
    rent = st.number_input("Monthly Rent", value=15000)

    area = st.number_input("Square Feet", value=1000)
    

    locality = st.selectbox("Locality", ['BTM Layout', 'Attibele', 'K R Puram ', 'Marathahalli',
                            'Indiranagar', 'Electronic City', 'Yalahanka', 'Malleshwaram',
                            'Jayanagar'])
    
    bathrooms = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)

    parking = st.selectbox("Parking", ['Bike', 'Bike and Car', 'Car', 'Missing'])

    facing = st.selectbox("Facing", ['North-West', 'East', 'North', 'West', 'North-East', 'South-East',
                          'South', 'Missing'])
    
    bhk = st.number_input("BHK", value=2, min_value=0, max_value=10, step=1)

    submitted = st.form_submit_button("Predict")
    

if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": area,
        "locality": locality,
        "bathrooms": bathrooms,
        "parking": parking if parking else "Missing",
        "facing": facing if facing else "Missing",
        "BHK": bhk
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")