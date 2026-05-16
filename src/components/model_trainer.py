import os 
import sys

from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from src.utils import evaluate_models

# Modelings
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

from sklearn.metrics import r2_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):   
        '''
        This function is responsible for training the model
        '''
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test = (train_array[:,:-1],
                                             train_array[:,-1],
                                             test_array[:,:-1],
                                             test_array[:,-1])
            models= {
                "Linear Regression": LinearRegression(),
                "Lasso Regression": Lasso(),
                "Ridge Regression": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree Regressor": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),   
                "Gradient Boosting Regressor": GradientBoostingRegressor()
            }

            model_report: dict = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models
            )

            # to get best score
            best_model_score = max(model_report.values())

            # to get best model name
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]
            logging.info("Best model found")


            if best_model_score < 0.6:
                raise CustomException("No best model found")
                logging.info("No Best model found in training and testing dataset")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            y_predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test,y_predicted)

            return r2_square

            # best_model_name = max(model_report, key=model_report.get)
            # best_model_score = model_report[best_model_name]
            # best_model = models[best_model_name]


        except Exception as e:
            raise CustomException(e,sys)
