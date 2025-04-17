import logging as log
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
from abc import ABC,abstractmethod
class Evalute(ABC):
    @abstractmethod
    def cal_metric(self,y_true: np.array,y_pred:np.array):
        pass
        # recall=recall_score(y_true,y_pred)
        # precision=precision_score(y_true,y_pred)
        # f1=f1_score(y_true,y_pred)
class Accuracy(Evalute):
    def cal_metric(self,y_true: np.array,y_pred:np.array):
        try:
            log.info("Calculating accuracy:")
            accuracy=accuracy_score(y_true,y_pred)
            log.info(f"Accuracy: {accuracy}")
            return accuracy
        except Exception as e:
            log.error(f"Error in Calculating Accuracy {e}")
            raise e
class Precesion(Evalute):
    def cal_metric(self,y_true: np.array,y_pred:np.array):
        try:
            log.info("Calculating Precision")
            precision=precision_score(y_true,y_pred,average="micro")
            log.info(f"Precision : {precision}")
            return precision
        except Exception as e:
            log.error(f"Error in calculating Precsion {e}")
            raise e
class Recall(Evalute):
    def cal_metric(self,y_true: np.array,y_pred:np.array):
        try:
            log.info("Calculating Recall Score")
            recall=recall_score(y_true,y_pred,average="micro")
            log.info(f"Recall : {recall}")
            return recall
        except Exception as e:
            log.error(f"Error in calculating recall {e}")
            raise e
class F1_Score(Evalute):
    def cal_metric(self,y_true: np.array,y_pred:np.array):
        try:
            log.info("Calculating F1_Score")
            f1=recall_score(y_true,y_pred,average="micro")
            log.info(f"F1 Score : {f1}")
            return f1
        except Exception as e:
            log.error(f"Error in calculating F1_Score {e}")
            raise e

if __name__=="__main__":
    from steps.clean_data import clean_df
    from steps.train_model import train_model
    from sklearn.metrics import classification_report
    x_train,x_test,y_train,y_test=clean_df(pd.read_csv(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv"),test_size=0.9)
    model=train_model(x_train,y_train)
    pred=model.predict(x_train)
    print(y_train)
    print(classification_report(y_train,pred))
    print(precision_score)
    # pre=Precesion()
    # print(pre.cal_metric(y_train,pred))
