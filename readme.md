# ❤️ HeartCare – Heart Disease Prediction Web App

**HeartCare** is a simple and fast web application built using **Streamlit** and **Scikit-learn**. It predicts the risk of heart disease based on medical input parameters.

---

## 📊 Dataset Used

The model is trained on the [Heart Disease UCI dataset](https://www.kaggle.com/datasets/ronitf/heart-disease-uci), containing:

- ✅ 303 patient records  
- ✅ 13 clinical features  
- ✅ Binary target variable (1 = disease, 0 = no disease)

---

## ⚙️ Features

- 🔍 Predicts heart disease risk using Logistic Regression  
- 📱 Easy-to-use web interface with Streamlit  
- ⚡ Fast prediction with trained `.pkl` model  
- 🧠 Uses 13 key medical inputs

---

## 🧠 Input Parameters

The model takes the following features:

| Feature       | Description                       |
|---------------|-----------------------------------|
| Age           | Age of the patient                |
| Sex           | 1 = Male, 0 = Female              |
| cp            | Chest pain type (0–3)            |
| trestbps      | Resting blood pressure (mm Hg)   |
| chol          | Serum cholesterol (mg/dl)        |
| fbs           | Fasting blood sugar > 120 mg/dl (1 = true) |
| restecg       | Resting electrocardiographic results |
| thalach       | Maximum heart rate achieved      |
| exang         | Exercise induced angina (1 = yes)|
| oldpeak       | ST depression induced by exercise|
| slope         | Slope of peak exercise ST segment|
| ca            | Number of major vessels (0–4)    |
| thal          | 3 = normal, 6 = fixed defect, 7 = reversible defect |

---

## 🚀 How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanyagupta31/heart-disease-predictor.git
   cd heart-disease-predictor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app:**
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Want to Retrain the Model?

You can retrain the model using the following Python code:

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("heart.csv")

X = df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

with open('heart_disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

---

## 🗂 Project Structure

```
heart-disease-predictor/
│
├── app.py                   # Streamlit app
├── heart.csv                # Dataset
├── heart_disease_model.pkl  # Trained ML model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📸 Screenshots

![Screenshot](Screenshot%202025-05-18%20131721.png)
![Screenshot](Screenshot%202025-05-18%20131802.png)

---

## 🧾 Requirements

- Python 3.7+
- pandas
- scikit-learn
- streamlit

---

## 📜 License

This project is licensed under the **MIT License**.

---

**Made with ❤️ by [Sanya Gupta](https://github.com/sanyagupta31)**  
