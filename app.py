from src.Ecotech_project.logger import logging 
from src.Ecotech_project.exception import CustomException
from src.Ecotech_project.components.data_ingestion import DataIngestion
from src.Ecotech_project.components.data_ingestion import DataIngestionConfig
from src.Ecotech_project.components.data_transformation import DataTransformationConfig, DataTransformation

import sys

if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data__ingestion = DataIngestion()
        train_data_path,test_data_path=data__ingestion.initiate_data_ingestion()

        data_transformation_config= DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    except Exception as e:
        logging.info("An exception occurred")
        raise CustomException(e, sys)