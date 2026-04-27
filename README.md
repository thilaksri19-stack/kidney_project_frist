# 🩺 Chronic Kidney Disease (CKD) Prediction Web App

## 📌 Project Overview

This project is a **Machine Learning Web Application** that predicts whether a person has **Chronic Kidney Disease (CKD)** or not based on medical parameters.

The model is trained using clinical data and deployed using a **Flask web framework** with a simple **HTML & CSS frontend**.

---

## 🚀 Features

* Predict CKD or Not CKD using input values
* User-friendly web interface
* Fast predictions using trained ML model (`.pkl`)
* Lightweight and easy to deploy

---

## 🧠 Input Features

The model uses the following medical parameters:

| Feature | Description                   |
| ------- | ----------------------------- |
| sc      | Serum Creatinine              |
| pot     | Potassium                     |
| dm      | Diabetes (0 = No, 1 = Yes)    |
| cad     | Coronary Artery Disease (0/1) |
| bu      | Blood Urea                    |
| sod     | Sodium                        |
| pe      | Pedal Edema (0/1)             |
| appet   | Appetite (0 = Good, 1 = Poor) |

---

## 🏗️ Project Structure

```
project/
│
├── app.py                 # Flask backend
├── ckd_model.pkl          # Trained ML model
│
├── templates/
│   └── index.html         # Frontend HTML
│
├── static/
│   └── style.css          # Styling
│
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/ckd-prediction.git
cd ckd-prediction
```

### 2️⃣ Install dependencies

```
pip install flask numpy scikit-learn
```

### 3️⃣ Run the application

```
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 How It Works

1. User enters medical values in the form
2. Data is sent to Flask backend
3. Model (`ckd_model.pkl`) processes input
4. Prediction is returned:

   * **CKD Detected**
   * **No CKD**

---

## 📦 Model Information

* Model saved using **Pickle (`.pkl`)**
* Trained on CKD dataset
* Binary Classification:

  * `1 → CKD`
  * `0 → Not CKD`

---

## 🌍 Deployment Options

You can deploy this app using:

* Render (Recommended)
* Heroku
* PythonAnywhere
* Local server with Gunicorn

### Run with Gunicorn:

```
gunicorn app:app
```

---

## ⚠️ Important Notes

* Ensure feature order matches training data
* Apply same preprocessing (if used)
* This model is for **educational purposes only**, not medical diagnosis

---

## 🔮 Future Improvements

* Add dropdown inputs instead of manual entry
* Show prediction probability
* Improve UI/UX design
* Add model performance metrics
* Deploy using Streamlit

---

## 👨‍💻 Author

**Your Name**

---

## 📄 License

This project is open-source and free to use for educational purposes.

---
