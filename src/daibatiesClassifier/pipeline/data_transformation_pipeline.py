from daibatiesClassifier.config import ConfigurationManager
from daibatiesClassifier.components import DataTransformation
from daibatiesClassifier import logger
STAGE = "DATA TRANSFORMATION"
def main():
    try:
        logger.info("{} {} {}".format("="*20,STAGE,"="*20))
        config = ConfigurationManager()
        data_trans_config = config.get_data_transform_config()
        data_transfor = DataTransformation(config=data_trans_config)
        data_transfor.transform_train()
        data_transfor.transform_test()
        logger.info("{}{}{}".format("="*20,STAGE + " " + "COMPLETED","="*20))

    except Exception as e:
        logger.info("There is error in data ingestion stage : " + str(e))
        raise e
       



if __name__ == "__main__":
    main()