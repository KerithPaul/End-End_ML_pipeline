from DS_Ops.config.configuration import ConfigurationManager
from DS_Ops.components.model_trainer import ModelTrainer
from DS_Ops import logger


STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e