import os
import sys
from src.Ecotech_project.exception import CustomException
from src.Ecotech_project.logger import logging
import pandas as pd
import pymysql
import pickle
import numpy as np
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading data from SQL database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection to database established successfully", mydb)
        df = pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)


def save_object(file_path, obj):   # ✅ Now it's reachable by Pylance
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
