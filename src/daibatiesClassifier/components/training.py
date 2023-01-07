import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle
from daibatiesClassifier.entity import DataTrainingConfig

class DataTraining:
    def __init__(self, config: DataTrainingConfig):
        self.config = config

    def train(self):

        df = pd.read_csv(self.config.train_data)

        X = df.drop('Outcome',axis=1)
        y = df['Outcome']

        sc = RobustScaler()

        d = sc.fit_transform(X)

        X = pd.DataFrame(d,columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'])

        skf = StratifiedKFold(n_splits=5)
        l = []
        for train_index, test_index in skf.split(X, y):

            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]
            ram = RandomForestClassifier()
            ram.fit(X_train,y_train)
            pred = ram.predict(X_test)
            l.append(accuracy_score(y_test,pred))

        print(np.mean(l))
        os.chdir(self.config.training_dir)
        with open('scaling.pickle', 'wb') as f:
    # write the object to the file
            pickle.dump(sc, f)
        with open('model.pickle', 'wb') as f:
    # write the object to the file
            pickle.dump(ram, f)