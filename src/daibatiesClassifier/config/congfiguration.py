from daibatiesClassifier.utils import *
from daibatiesClassifier.utils import read_yaml
from daibatiesClassifier.constants import *
from daibatiesClassifier.entity import DataIngestionConfig


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