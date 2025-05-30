from DS_Ops import logger
from DS_Ops.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from DS_Ops.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from DS_Ops.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from DS_Ops.pipeline.stage_04_model_training import ModelTrainingPipeline
from DS_Ops.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e