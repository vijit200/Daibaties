from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source",
    "unzip_dir",
    "train_dir",
    "test_dir"
])


DataTransformationConfig = namedtuple("DataTransformationConfig", [
    "train_data",
    "test_data",
    "transform_dir"
])

DataTrainingConfig = namedtuple("DataTrainingConfig", [
    "train_data",
    "training_dir"
])