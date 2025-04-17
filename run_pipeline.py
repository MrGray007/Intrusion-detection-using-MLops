from pipeline.pipeline_run import pipeline
from zenml.client import Client
if __name__=="__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    pipeline(data_path="/mnt/c/Users/mahesh/Desktop/zenml_wsl/dataset/df_50k.csv",test_size=0.3)
