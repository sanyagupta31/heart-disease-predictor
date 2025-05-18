import streamlit as st
import numpy as np
import pickle

# Load the model
with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("💓 Heart Disease Prediction App")
st.write("Enter the required information to predict the risk of heart disease:")

# Input fields
age = st.number_input("Age", 1, 120, 29)
sex = st.selectbox('Sex', ['Female', 'Male'])
cp = st.selectbox('Chest pain type', [0, 1, 2, 3])
trestbps = st.number_input("Resting blood pressure", 1, 200, 130)
chol = st.number_input("Cholesterol", 1, 600, 200)
fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', ['No', 'Yes'])
restecg = st.selectbox('Resting electrocardiographic results', [0, 1, 2])
thalach = st.number_input("Maximum heart rate achieved", 1, 250, 150)
exang = st.selectbox('Exercise induced angina', ['No', 'Yes'])
oldpeak = st.number_input("ST depression induced by exercise relative to rest", 0.0, 10.0, 1.0)
slope = st.selectbox('Slope of the peak exercise ST segment', [0, 1, 2])
ca = st.selectbox('Number of major vessels (0-3) colored by fluoroscopy', [0, 1, 2, 3])
thal = st.selectbox('Thalassemia', ['Normal', 'Fixed defect', 'Reversible defect'])

# Map categorical values to numerical values
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'Yes' else 0
exang = 1 if exang == 'Yes' else 0
thal_dict = {'Normal': 1, 'Fixed defect': 2, 'Reversible defect': 3}
thal = thal_dict[thal]

# Prediction
if st.button('Predict'):
    input_data = np.array([[float(age), sex, cp, float(trestbps), float(chol), fbs, 
                            restecg, float(thalach), exang, float(oldpeak), slope, 
                            ca, thal]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('⚠️ The person is likely to have heart disease.')
    else:
        st.success('✅ The person is unlikely to have heart disease.')
