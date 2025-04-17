from pipeline.deployment import (
       continous_deployment,
       predictor
)
import click
DEPLOY="deploy"
PREDICT="predict" ; DEPLOY_AND_PREDICT='deploy_and_predict'
@click.command
@click.option(
       "--config",
       "-c",
       type=click.Choice([DEPLOY,PREDICT,DEPLOY_AND_PREDICT]),
       default=DEPLOY,
       help="Optionally you can choose to only run the deployment "
            "pipeline to train and deploy a model (`deploy`), or to "
            "only run a prediction against the deployed model "
            "(`predict`). By default both will be run "
            "(`deploy_and_predict`).",

)
def run_pipeline(config:str):
       if config =="deploy" or config =='deploy_and_predict':
             continous_deployment(data_path=r"/mnt/c/Users/mahesh/Desktop/zenml_wsl/dataset/df_50k.csv",worker=3,timeout=100)
       if config=="predict" or config =='deploy_and_predict':
             predictor(pipeline_name="continous_deployment",pipeline_step_name="mlflow_model_deployer_step")
             
             
if __name__=="__main__":
    run_pipeline()
