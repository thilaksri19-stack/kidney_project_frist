from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('ckd_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [
        float(request.form['sc']),
        float(request.form['pot']),
        float(request.form['dm']),
        float(request.form['cad']),
        float(request.form['bu']),
        float(request.form['sod']),
        float(request.form['pe']),
        float(request.form['appet'])
    ]

    final_input = np.array([data])

    prediction = model.predict(final_input)

    if prediction[0] == 1:
        result = "CKD Detected"
    else:
        result = "No CKD"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)