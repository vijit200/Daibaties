from daibatiesClassifier.config import ConfigurationManager
from daibatiesClassifier.components import DataIngestion
from daibatiesClassifier import logger
STAGE = "DATA INGESTION"
def main():
    try:
        logger.info("{} {} {}".format("="*20,STAGE,"="*20))
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.unzip_and_clean()
        data_ingestion.train_test_devide()
        logger.info("{}{}{}".format("="*20,STAGE + " " + "COMPLETED","="*20))

    except Exception as e:
        logger.info("There is error in data ingestion stage : " + str(e))
        raise e
       



if __name__ == "__main__":
    main()