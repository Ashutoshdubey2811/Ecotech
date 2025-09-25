from src.Ecotech_project.logger import logging 
from src.Ecotech_project.exception import CustomException
from src.Ecotech_project.components.data_ingestion import DataIngestion
from src.Ecotech_project.components.data_ingestion import DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data__ingestion = DataIngestion()
        data__ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("An exception occurred")
        raise CustomException(e, sys)