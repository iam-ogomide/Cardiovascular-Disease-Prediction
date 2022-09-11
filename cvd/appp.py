# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.externals import joblib

# Load the KNN model
filename = 'cvd.pkl'
classi = pickle.load(open(filename, 'rb'))

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        agr = request.form['age']
        gen = request.form['sex']
        cpt = request.form['cp']
        rbs = request.form['trestbps']
        chl = request.form['chol']
        fb = request.form['fbs']
        ecg = request.form['restecg']
        mhr = request.form['thalach']
        eia = request.form['exang']
        std = request.form['oldpeak']
        sts = request.form['slope']
        major = request.form['ca']
        thalas = request.form['thal']
        data = np.array([[agr ,gen, cpt , rbs , chl , fb , ecg , mhr , eia , std , sts , major , thalas ]])
       
        inputFeature = np.asarray(data).reshape(1,-1)
        my_prediction = classi.predict(inputFeature)
        
        return render_template('result.html', prediction=my_prediction[0])

if __name__ == '__main__':
	app.run(debug=True)
