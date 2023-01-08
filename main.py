from flask import Flask,render_template,request
import pickle


import numpy as np
model = pickle.load(open(r'artifacts\training\model.pickle','rb'))
processing = pickle.load(open(r'artifacts\training\scaling.pickle','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
@app.route('/predict',methods = ['POST'])

def predict():
    if request.method == 'POST':
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])
        l =np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        s = l.reshape(1,-1)
        scaling = processing.transform(s)
        model_eval = model.predict(scaling)[0]
        if model_eval == 0:
            return render_template('index.html',predict_daibaties = "No")
        else:
            return render_template('index.html',predict_daibaties = "Yes")


if __name__ == '__main__':
    app.run(debug=True)