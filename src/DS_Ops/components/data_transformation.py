import os
from DS_Ops import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from DS_Ops.entity.config_entity import DataTransformationConfig


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    def train_test_splitting(self):

        try:
            data = pd.read_csv(self.config.data_path)

            train, test = train_test_split(data)

            train.to_csv(os.path.join(self.config.root_dir, "train_csv"),index = False)
            test.to_csv(os.path.join(self.config.root_dir, "test_csv"),index = False)

            logger.info("Splitted data into training and test sets")
            logger.info(train.shape)
            logger.info(test.shape)

            print(train.shape)
            print(test.shape)

        except Exception as e:
            raise e