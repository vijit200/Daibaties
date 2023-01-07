from daibatiesClassifier.config import ConfigurationManager
from daibatiesClassifier.components import DataTraining
from daibatiesClassifier import logger
STAGE = "Model Training"
def main():
    try:
        logger.info("{} {} {}".format("="*20,STAGE,"="*20))
        config = ConfigurationManager()
        data_train_config = config.get_data_training_config()
        data_train = DataTraining(config=data_train_config)
        data_train.train()
        logger.info("{}{}{}".format("="*20,STAGE + " " + "COMPLETED","="*20))

    except Exception as e:
        logger.info("There is error in data ingestion stage : " + str(e))
        raise e
       



if __name__ == "__main__":
    main()