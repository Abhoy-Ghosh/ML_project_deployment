# =========================================================
# IMPORT REQUIRED MODULES
# =========================================================

import os
# Used for:
# - folder creation
# - file path handling
# - OS-independent path management

import sys
# Used for:
# - capturing detailed exception traceback
# - works with CustomException class

from src.exception import CustomException
# Importing our custom exception handler
# Gives professional readable error messages

from src.logger import logging
# Importing configured logging system
# Used to track execution flow and debugging

import pandas as pd
# Used for dataframe operations

from sklearn.model_selection import train_test_split
# Used to split dataset into:
# - training data
# - testing data

from dataclasses import dataclass
# Used to create configuration class easily
# Automatically generates constructor (__init__)


# =========================================================
# CONFIGURATION CLASS
# =========================================================

@dataclass
class DataIngestionConfig:

    # Path where training dataset will be stored
    train_data_path: str = os.path.join('artifacts', "train.csv")

    # Path where testing dataset will be stored
    test_data_path: str = os.path.join('artifacts', "test.csv")

    # Path where raw/original dataset copy will be stored
    raw_data_path: str = os.path.join('artifacts', "data.csv")


# =========================================================
# DATA INGESTION CLASS
# =========================================================

class DataIngestion:

    # Constructor method
    # Automatically runs when object is created

    def __init__(self):

        # Creating configuration object

        self.ingestion_config = DataIngestionConfig()


    # =====================================================
    # MAIN DATA INGESTION METHOD
    # =====================================================

    def initiate_data_ingestion(self):

        # Log entry message
        # Helps track pipeline execution

        logging.info("Entered the data ingestion method or component")

        try:

            # =================================================
            # STEP 1 : READ DATASET
            # =================================================

            # Reading CSV dataset into pandas dataframe

            df = pd.read_csv(r'notebook\data\stud.csv')

            # Log successful dataset loading

            logging.info('Read the dataset as dataframe')


            # =================================================
            # STEP 2 : CREATE ARTIFACTS FOLDER
            # =================================================

            # self.ingestion_config.raw_data_path
            # gives:
            # artifacts/data.csv

            # os.path.dirname(...)
            # extracts ONLY folder name:
            # artifacts

            # os.makedirs(...)
            # creates folder if it doesn't exist

            # exist_ok=True
            # prevents error if folder already exists

            os.makedirs(
                os.path.dirname(self.ingestion_config.raw_data_path),
                exist_ok=True
            )


            # =================================================
            # STEP 3 : SAVE RAW DATA
            # =================================================

            # Saving original dataset copy

            # index=False
            # avoids saving dataframe index column

            # header=True
            # keeps column names

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )


            # =================================================
            # STEP 4 : TRAIN TEST SPLIT
            # =================================================

            logging.info("Train test split initiated")

            # Splitting dataset:
            # 80% train
            # 20% test

            # random_state=42
            # ensures same split every run
            # (reproducibility)

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )


            # =================================================
            # STEP 5 : SAVE TRAIN DATA
            # =================================================

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )


            # =================================================
            # STEP 6 : SAVE TEST DATA
            # =================================================

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )


            # =================================================
            # STEP 7 : LOG COMPLETION
            # =================================================

            logging.info("Ingestion of the data is completed")


            # =================================================
            # STEP 8 : RETURN FILE PATHS
            # =================================================

            # Returning train and test file paths

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        # =====================================================
        # EXCEPTION HANDLING
        # =====================================================

        except Exception as e:

            # If any error occurs:
            # - catch error
            # - raise custom readable exception

            raise CustomException(e, sys)


# =========================================================
# MAIN EXECUTION BLOCK
# =========================================================

# This block runs ONLY when file executed directly

if __name__ == "__main__":

    # Creating object of DataIngestion class

    obj = DataIngestion()

    # Calling ingestion pipeline

    train_path, test_path = obj.initiate_data_ingestion()

    # Printing returned paths

    print(train_path)
    print(test_path)


# =========================================================
# COMPLETE FLOW OF THIS FILE
# =========================================================

"""
            DATA INGESTION FLOW

                CSV Dataset
                      ↓
          Read using pandas
                      ↓
         Create artifacts folder
                      ↓
           Save raw dataset copy
                      ↓
            Train-Test Split
             (80% / 20%)
                      ↓
          Save train.csv file
                      ↓
           Save test.csv file
                      ↓
           Return file paths
                      ↓
      Used by Transformation Pipeline


=========================================================

WHY THIS FILE EXISTS?

Purpose of Data Ingestion:

1. Read dataset
2. Create folder structure
3. Split dataset
4. Save train/test data
5. Prepare pipeline input
6. Keep workflow modular

=========================================================

WHY MODULAR STRUCTURE?

Instead of writing everything in one notebook:

- easier debugging
- reusable code
- scalable architecture
- production-ready design
- easier deployment

=========================================================
"""