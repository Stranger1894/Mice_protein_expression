from micepe.entity import artifact_entity,config_entity
from micepe.exception import MiceException
from micepe.logger import logging
from typing import Optional
import os,sys 
from sklearn.linear_model import LogisticRegression
from micepe import utils
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, KFold


class ModelTrainer:


    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig,
                data_transformation_artifact:artifact_entity.DataTransformationArtifact
                ):
        try:
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact

        except Exception as e:
            raise MiceException(e, sys)

    def fine_tune(self,x,y):
        try:
            logging.info(f"Initiating hyperparameter tuning")
            param_grid = [
                {'penalty' : ['l1', 'l2', 'elasticnet', 'none'],
                'C' : [100, 10, 1.0, 0.1, 0.01],
                'solver' : ['lbfgs','newton-cg','liblinear','sag','saga'],
                'max_iter' : [100, 1000,2500, 5000]
                }]
            kfold_validation = KFold(10)
            model = LogisticRegression()
            grid_search = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=kfold_validation)

            logging.info(f"Fitting grid search CV to find best parameters")
            grid_result = grid_search.fit(x, y)

            best_params = grid_result.best_params_
            best_score = grid_result.best_score_
            logging.info(f"Best accuracy score achieved after hyperparameter tuning = {best_score}")

            return best_params
       
        except Exception as e:
            raise MiceException(e, sys)

    def train_model(self,x,y):
        try:
            best_params = ModelTrainer.fine_tune(self, x, y)

            logging.info(f"Fitting the model with best parameters obtained after hyperparameter tuning")
            logreg =  LogisticRegression(C= best_params['C'], max_iter= best_params['max_iter'], \
                        penalty= best_params['penalty'], solver= best_params['solver'])
            logreg.fit(x,y)
            return logreg
        except Exception as e:
            raise MiceException(e, sys)

    """def train_model(self,x,y):
        try:
            logreg =  LogisticRegression()
            logreg.fit(x,y)
            return logreg
        except Exception as e:
            raise MiceException(e, sys)"""


    def initiate_model_trainer(self,)->artifact_entity.ModelTrainerArtifact:
        try:
            logging.info(f"Loading train and test array.")
            train_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)

            logging.info(f"Splitting input and target feature from both train and test arr.")
            x_train,y_train = train_arr[:,:-1],train_arr[:,-1]
            x_test,y_test = test_arr[:,:-1],test_arr[:,-1]

            logging.info(f"Train the model")
            model = self.train_model(x=x_train,y=y_train)

            logging.info(f"Calculating accuracy train score")
            yhat_train = model.predict(x_train)
            accuracy_train_score  =accuracy_score(y_true=y_train, y_pred=yhat_train)

            logging.info(f"Calculating accuracy test score")
            yhat_test = model.predict(x_test)
            accuracy_test_score  =accuracy_score(y_true=y_test, y_pred=yhat_test)
            
            logging.info(f"train score:{accuracy_train_score} and tests score {accuracy_test_score}")
            #check for overfitting or underfiiting or expected score
            logging.info(f"Checking if our model is underfitting or not")
            if accuracy_test_score<self.model_trainer_config.expected_score:
                raise Exception(f"Model is not good as it is not able to give \
                expected accuracy: {self.model_trainer_config.expected_score}: model actual score: {accuracy_test_score}")

            logging.info(f"Checking if our model is overfiiting or not")
            diff = abs(accuracy_train_score-accuracy_test_score)

            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train and test score diff: {diff} is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")

            #save the trained model
            logging.info(f"Saving mode object")
            utils.save_object(file_path=self.model_trainer_config.model_path, obj=model)

            #prepare artifact
            logging.info(f"Prepare the artifact")
            model_trainer_artifact  = artifact_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path, 
            accuracy_train_score=accuracy_train_score, accuracy_test_score=accuracy_test_score)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise MiceException(e, sys)