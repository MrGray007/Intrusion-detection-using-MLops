import logging
import mlflow
from src.model_evalution import Accuracy,Precesion,Recall,F1_Score
from typing import Tuple
from typing_extensions import Annotated
from zenml import step
from zenml.client import Client
experiment_tracker=Client().active_stack.experiment_tracker
print(experiment_tracker.name)
@step(experiment_tracker=experiment_tracker.name)
def evalute_model(model,x_test,y_test)->Tuple[
    Annotated[float,"accuracy"],
    Annotated[float,"precision"],
    Annotated[float,"recall"],
    Annotated[float,"f1_score"]
]:
    try:
        pred=model.predict(x_test)
        acc_class=Accuracy()
        accuracy=acc_class.cal_metric(y_test,pred)
        mlflow.log_metric("accuracy",accuracy)
        prec_class=Precesion()
        precision=prec_class.cal_metric(y_test,pred)
        mlflow.log_metric("precision",precision)
        rec_class=Recall()
        recall=rec_class.cal_metric(y_test,pred)
        mlflow.log_metric("recall",recall)
        f1_class=F1_Score()
        f1_score=f1_class.cal_metric(y_test,pred)
        mlflow.log_metric("f1_score",f1_score)
        return accuracy,precision,recall,f1_score
    except Exception as e:
        logging.error(f"Error in Evaluting model {e}")
        raise e
# if __name__=="__main__":
#     import pickle as pk
#     model=pk.load(open(r"C:\Users\mahesh\Desktop\ids\model.pickel",'rb'))
#     from steps.clean_data import clean_df
#     model.p
#     x_train, x_test, y_train, y_test = clean_df(pd.read_csv(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv"),test_size=0.9)
#     metrics=evalute_model(model,x_train,y_train)
#     acc=
