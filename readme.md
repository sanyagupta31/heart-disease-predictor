 

````markdown
# ❤️ Heart Disease Prediction App

This is a simple web app built using **Streamlit** and **Scikit-learn** to predict the likelihood of heart disease based on user inputs.

---

## 📊 Dataset

The model is trained on the [Heart Disease UCI dataset](https://www.kaggle.com/datasets/ronitf/heart-disease-uci), which includes 303 samples and 13 clinical features.

---

## 🚀 Features

- Predicts heart disease risk based on 13 medical attributes.
- Clean and simple UI with Streamlit.
- Model built using Logistic Regression.
- Fast and lightweight app.

---

## 🧠 Input Features

The app takes the following inputs:

1. Age
2. Sex
3. Chest Pain Type (`cp`)
4. Resting Blood Pressure (`trestbps`)
5. Cholesterol (`chol`)
6. Fasting Blood Sugar (`fbs`)
7. Resting ECG (`restecg`)
8. Maximum Heart Rate (`thalach`)
9. Exercise Induced Angina (`exang`)
10. ST Depression (`oldpeak`)
11. Slope of ST (`slope`)
12. Number of Major Vessels (`ca`)
13. Thalassemia (`thal`)

---

## 🛠 Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/sanyagupta31/heart-disease-predictor.git
    cd heart-disease-predictor
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## 🧪 Model Training (Optional)

If you'd like to retrain the model:

```python
# See model_training.py or include this code in a new notebook
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
````

---

## 📎 File Structure

```
heart-disease-predictor/
│
├── app.py                   # Streamlit app
├── heart.csv                # Dataset
├── heart_disease_model.pkl  # Trained model
├── README.md                # You are here!
└── requirements.txt         # Python packages
```

---

## 📸 Screenshots

Screenshot 2025-05-18 131721.png
Screenshot 2025-05-18 131802.png

---

## 📌 Requirements

* Python 3.7+
* scikit-learn
* pandas
* streamlit

---



## ✅ License

This project is open-source and free to use under the MIT License.

```

---

Let me know if you'd like a customized version with your name, GitHub profile link, or screenshots.
```
