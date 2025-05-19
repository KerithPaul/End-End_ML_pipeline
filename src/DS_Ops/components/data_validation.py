import os
import pandas as pd
from DS_Ops import logger

from DS_Ops.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self) -> bool:
        """
        Validate all columns in the dataset
        """

        try:
            validation_status = None

            logger.info("Validating all columns in the dataset")
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for column in all_cols:
                if column not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Column is missing from the schema\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Column is present in the schema\n")

            return validation_status
        
        except Exception as e:
            raise e