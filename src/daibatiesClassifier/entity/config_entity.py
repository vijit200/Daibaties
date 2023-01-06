from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source",
    "unzip_dir",
    "train_dir",
    "test_dir"
])