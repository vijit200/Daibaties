import os
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from daibatiesClassifier.entity import DataEvaluationConfig
import pickle

class DataEvaluation:
    def __init__(self, config: DataEvaluationConfig):
        self.config = config

    def Eval(self):

        df = pd.read_csv(self.config.test_data)

        X = df.drop('Outcome',axis=1)
        y = df['Outcome']

        sc = pickle.load(open(self.config.scale,'rb'))
        model = pickle.load(open(self.config.model,'rb'))



        d = sc.transform(X)
        

        X = pd.DataFrame(d,columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'])

        ms = model.predict(X)
        #print(ms)
        #print(list(y))

        print(accuracy_score(y,ms))