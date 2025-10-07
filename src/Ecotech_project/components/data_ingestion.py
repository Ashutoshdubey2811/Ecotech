import os
import sys
import pandas as pd
from src.Ecotech_project.logger import logging
from src.Ecotech_project.exception import CustomException
from src.Ecotech_project.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Read data from MySQL
            df = pd.read_csv(os.path.join('notebook/data','raw.csv'))
            logging.info("Reading completed from MySQL database")

            # Ensure artifacts directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Train-test split
            df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test data
            df_train.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            df_test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
