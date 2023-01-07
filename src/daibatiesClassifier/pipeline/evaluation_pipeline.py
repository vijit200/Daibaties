from daibatiesClassifier.config import ConfigurationManager
from daibatiesClassifier.components import DataEvaluation
from daibatiesClassifier import logger
STAGE = "Model Evaluation"
def main():
    try:
        logger.info("{} {} {}".format("="*20,STAGE,"="*20))
        config = ConfigurationManager()
        data_eval_config = config.get_data_evaluation_config()
        data_eval = DataEvaluation(config=data_eval_config)
        data_eval.Eval()
        logger.info("{}{}{}".format("="*20,STAGE + " " + "COMPLETED","="*20))

    except Exception as e:
        logger.info("There is error in data ingestion stage : " + str(e))
        raise e
       



if __name__ == "__main__":
    main()