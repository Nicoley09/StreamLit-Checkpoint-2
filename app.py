import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('financial_inclusion_model.pkl')

st.set_page_config(page_title="Financial Inclusion Predictor", page_icon="💰", layout="centered")
st.title("💰 Financial Inclusion Predictor in East Africa")
st.write("Predict whether an individual is likely to have a bank account.")

st.sidebar.header("Enter Individual Details")

# --------------------
# Input fields
# --------------------
country = st.sidebar.selectbox("Country", [0,1,2])  # Adjust based on encoding
year = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2022)
location_type = st.sidebar.selectbox("Location Type", ["Urban", "Rural"])
cellphone_access = st.sidebar.selectbox("Cellphone Access", ["No", "Yes"])
household_size = st.sidebar.number_input("Household Size", min_value=1, max_value=20, value=3)
age_of_respondent = st.sidebar.number_input("Age of Respondent", min_value=18, max_value=100, value=25)
gender_of_respondent = st.sidebar.selectbox("Gender", ["Male", "Female"])
relationship_with_head = st.sidebar.selectbox("Relationship with Head", ["Head","Spouse","Child","Other"])
marital_status = st.sidebar.selectbox("Marital Status", ["Single","Married","Divorced","Widowed"])
education_level = st.sidebar.selectbox("Education Level", ["None","Primary","Secondary","Tertiary"])
job_type = st.sidebar.selectbox("Job Type", ["Unemployed","Salaried","Self-employed","Other"])

# --------------------
# Encode categorical variables
# --------------------
location_map = {"Urban":0, "Rural":1}
cellphone_map = {"No":0, "Yes":1}
gender_map = {"Male":0, "Female":1}
relationship_map = {"Head":0,"Spouse":1,"Child":2,"Other":3}
marital_map = {"Single":0,"Married":1,"Divorced":2,"Widowed":3}
education_map = {"None":0,"Primary":1,"Secondary":2,"Tertiary":3}
job_map = {"Unemployed":0,"Salaried":1,"Self-employed":2,"Other":3}

# --------------------
# Create input DataFrame in exact order
# --------------------

# Example uniqueid placeholder
uniqueid = 1  # Can be any integer; just to match training columns

feature_columns = [
    "country","year","uniqueid","location_type","cellphone_access","household_size",
    "age_of_respondent","gender_of_respondent","relationship_with_head",
    "marital_status","education_level","job_type"
]

input_data = pd.DataFrame([[ 
    country,
    year,
    uniqueid,  # Added to match training features
    location_map[location_type],
    cellphone_map[cellphone_access],
    household_size,
    age_of_respondent,
    gender_map[gender_of_respondent],
    relationship_map[relationship_with_head],
    marital_map[marital_status],
    education_map[education_level],
    job_map[job_type]
]], columns=feature_columns)

# --------------------
# Prediction
# --------------------
if st.button("Predict"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    
    if prediction[0] == 1:
        st.success(f"✅ Likely to have a bank account (Probability: {probability:.2f})")
    else:
        st.error(f"❌ Unlikely to have a bank account (Probability: {probability:.2f})")
