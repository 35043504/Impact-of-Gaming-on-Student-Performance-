import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🎮 Gaming Behavior CGPA Prediction")

st.write("Enter details to predict CGPA")

age = st.number_input("Age")
gaming_hours = st.number_input("Average Gaming Hours", 0, 12)
sleep = st.number_input("Sleep Hours", 0, 12)
if st.button("Predict CGPA"):
    
    # Create empty feature vector with 27 features
    features = np.zeros((1, 27))
    
    # Fill some example features (index positions arbitrary for demo)
    features[0,0] = age
    features[0,1] = gaming_hours
    features[0,2] = sleep
    
    prediction = model.predict(features)

    st.success(f"Predicted CGPA: {prediction[0]:.2f}")    