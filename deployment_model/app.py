import streamlit as st
import pandas as pd
import pickle

# LOAD MODEL
model = pickle.load(open("deployment_model/calorie_model.pkl", "rb"))

# TITLE
st.title("Calories Burn Prediction")

# USER INPUTS
gender_text = st.selectbox("Gender",["Male", "Female"])
age = st.number_input("Age")
height = st.number_input("Height (cm)",min_value=1.0)
weight = st.number_input("Weight (kg)")
duration = st.number_input("Duration (minutes)")
heart_rate = st.number_input("Heart Rate")
body_temp = st.number_input("Body Temperature")

# CONVERT GENDER
gender = 1 if gender_text == "Male" else 0

# BMI FEATURE
bmi = weight / ((height / 100) ** 2)

# PREDICT BUTTON
if st.button("Predict Calories"):

    input_df = pd.DataFrame([{
        'Gender': gender,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Duration': duration,
        'Heart_Rate': heart_rate,
        'Body_Temp': body_temp,
        'BMI': bmi }])

    prediction = model.predict(input_df)
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f}")
