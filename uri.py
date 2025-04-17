from zenml.client import Client
if __name__=="__main__":
    print(f"mlflow ui  --backend-store-uri {Client().active_stack.experiment_tracker.get_tracking_uri()}")