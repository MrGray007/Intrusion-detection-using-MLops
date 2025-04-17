import mlflow
import pandas as pd
import logging as log
from src.model_train import Votingclassifier,RandomForest
from sklearn.ensemble import VotingClassifier
from zenml import step
from zenml.client import Client
from sklearn.base import ClassifierMixin
experiment=Client().active_stack.experiment_tracker
print(experiment.name)
@step(experiment_tracker=experiment.name)
def train_model(x_train: pd.DataFrame,y_train: pd.DataFrame,model_name='voteclassifier') -> ClassifierMixin:
    try:
        log.info("Model Training Started...........................")
        print("Model Training Started...........................")
        if model_name=='voteclassifier':
            mlflow.sklearn.autolog()
            model=Votingclassifier()
            model=model.train(x_train,y_train)
            return model
        elif model_name == "randomforest":
            mlflow.sklearn.autolog()
            model=RandomForest()
            model=model.train(x_train,y_train)
            return model
        if isinstance(module,ClassifierMixin):
            raise TypeError("The model is not ClassifierMixin")
    except Exception as e:
        log.error("Error in model Training")
        raise e
if __name__=="__main__":
    from steps.clean_data import clean_df
    x_train,x_test,y_train,y_test=clean_df(pd.read_csv(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv"),test_size=0.9)
    model=train_model(x_train,y_train)
    print(type(model))
    print(isinstance(model,ClassifierMixin))


