import os
from zipfile import ZipFile
import pandas as pd
from daibatiesClassifier.utils import *
from daibatiesClassifier.utils import read_yaml
from daibatiesClassifier.constants import *
from sklearn.model_selection import StratifiedShuffleSplit
from daibatiesClassifier.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def unzip_and_clean(self):
        with ZipFile(file=self.config.source, mode="r") as zf:
            zf.extractall(self.config.unzip_dir)


    def train_test_devide(self):

        name = os.listdir(self.config.unzip_dir)[0]
        s = os.path.join(self.config.unzip_dir,name)
        df = pd.read_csv(s)

        create_directories([self.config.train_dir])
        create_directories([self.config.test_dir])

        strat_train_set = None
        strat_test_set = None

        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
        for train_index,test_index in split.split(df, df["Outcome"]):
            strat_train_set = df.loc[train_index]
            strat_test_set = df.loc[test_index] 

        train_path = os.path.join(self.config.train_dir,"train.csv")
        test_path = os.path.join(self.config.test_dir,"test.csv")

        strat_train_set.to_csv(train_path,index=False)
        strat_test_set.to_csv(test_path,index=False)