import os
import pandas as pd
import numpy as np
from daibatiesClassifier.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_train(self):

        df = pd.read_csv(self.config.train_data)

        col=['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI']
        for i in col:
            df[i].replace(0,np.nan, inplace = True)

        for i in col:
            if df[i].isnull().sum() > 0:
                df[i] = df[i].fillna(df[i].median())

        print(df.isnull().sum())
        s = os.path.join(self.config.transform_dir,"train_main.csv")
        df.to_csv(s,index=False)      

    def transform_test(self):

        df = pd.read_csv(self.config.test_data)

        col=['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI']
        for i in col:
            df[i].replace(0,np.nan, inplace = True)

        for i in col:
            if df[i].isnull().sum() > 0:
                df[i] = df[i].fillna(df[i].median())

        print(df.isnull().sum())
        s = os.path.join(self.config.transform_dir,"test_main.csv")
        df.to_csv(s,index=False)  
    