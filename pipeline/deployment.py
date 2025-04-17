import json
import pandas as pd
import numpy as np
from zenml import pipeline,step
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.config import DockerSettings
from zenml.integrations.constants import MLFLOW
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import MLFlowModelDeployer
from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
# from zenml.steps import BaseParameters
docker_settings= DockerSettings(required_integrations=[MLFLOW])
from steps.indest_data import ingest_data
from steps.clean_data import clean_df
from steps.train_model import train_model
from steps.evaluate_model import evalute_model
# class DeploymentCriteria:
#     min_accuracy : float=0.9
#     min_precision : float=0.6

# @step
# def deployment_triger(accuracy: float,precision:float,config = DeploymentCriteria())->bool:
#     return accuracy>=config.min_accuracy and precision>=config.min_precision

@step
def predictor_loader(
    pipeline_name:str,
    step_name:str,
    running:bool,
    model_name:str='model'
)->MLFlowDeploymentService:
    mlflow_model_depl_com=MLFlowModelDeployer.get_active_model_deployer()
    existing_services=mlflow_model_depl_com.find_model_server(
        pipeline_name=pipeline_name,
        pipeline_step_name=step_name,
        model_name=model_name,
        running=running
    )

    if not existing_services:
        raise RuntimeError(
            f'''No mlflow deployment service found for pipeline {pipeline_name} "
            step {step_name} and model {model_name} 
            pipeline for the {model_name} is currently 
            running'''
        )
    print(existing_services)
    return existing_services[0]
@step
def data_prep(data_path:str="/mnt/c/Users/mahesh/Desktop/zenml_wsl/dataset/df_50k.csv")->np.ndarray:
    data=pd.read_csv(data_path)
    col_list=['Timestamp', 'Bwd PSH Flags', 'Fwd URG Flags', 'Bwd URG Flags', 'CWE Flag Count','Fwd Byts/b Avg', 'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg', 'Bwd Pkts/b Avg','Bwd Blk Rate Avg']
    if col_list in list(data.columns):
        data=data.drop(columns=col_list)
    if "Label" in list(data.columns):
        data=data.drop(columns='Label')
    json_list=json.loads(json.dumps(list(data.T.to_dict().values())))
    data=np.array(json_list)
    return data



@step
def predict(
    service:MLFlowDeploymentService,
    data:np.ndarray
)-> np.ndarray:
    # data=data_prep(data_path="/mnt/c/Users/mahesh/Desktop/zenml_wsl/dataset/df_50k.csv")
    service.start(timeout=30)
    pred=service.predict(data)
    return pred
    

@pipeline( enable_cache=True,settings={"docker":docker_settings})
def continous_deployment(
        data_path :str,
        worker:int=1,
        timeout : int =DEFAULT_SERVICE_START_STOP_TIMEOUT
):
    df=ingest_data(data_path)
    x_train,x_test,y_train,y_test=clean_df(df,test_size=0.5)
    model=train_model(x_train,y_train,model_name="randomforest")
    print("deploy_start___")
    accuracy,precision,recall,f1=evalute_model(model,x_test,y_test)
    print(accuracy,precision)
    print("deploy_start")
    deploy_decision=True
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deploy_decision,
        workers=worker,
        timeout=timeout
    )

@pipeline(enable_cache=False,settings={"docker":docker_settings})
def predictor(pipeline_name:str,pipeline_step_name:str,data_path:str="/mnt/c/Users/mahesh/Desktop/zenml_wsl/dataset/df_50k.csv"):
    data=data_prep(data_path)
    service=predictor_loader(pipeline_name=pipeline_name,step_name=pipeline_step_name,running=False)
    pred=predict(service=service,data=data)
    return pred
if __name__=="__main__":
    # continous_deployment(data_path=r"C:\Users\mahesh\Desktop\zenml_wsl\dataset\df_50k.csv",worker=3,timeout=100)
    predictor(pipeline_name="continous_deployment",pipeline_step_name="mlflow_stack_threat")

