from daibatiesClassifier.utils import *
from daibatiesClassifier.utils import read_yaml
from daibatiesClassifier.constants import *
from daibatiesClassifier.entity import DataIngestionConfig,DataTransformationConfig,DataTrainingConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH

    ):
        self.config = read_yaml(config_filepath)
        #self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories(["artifacts/data_ingestion"])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source = config.source,
            unzip_dir= config.unzip_dir,
            train_dir=config.train_dir,
            test_dir= config.test_dir
        )

        return data_ingestion_config

    def get_data_transform_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories(["artifacts/data_transform"])

        data_transformation_config = DataTransformationConfig(
            train_data=  config.train_data,
            test_data=  config.test_data,
            transform_dir= config.transform_dir
        )

        return data_transformation_config



    def get_data_training_config(self) -> DataTrainingConfig:
        config = self.config.model_training
        
        create_directories(["artifacts/training"])

        data_training_config = DataTrainingConfig(
            train_data = config.train_data,
            training_dir = config.training_dir
        )

        return data_training_config