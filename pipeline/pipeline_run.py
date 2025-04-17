from steps.clean_data import clean_df
from steps.indest_data import ingest_data
from steps.train_model import train_model
from steps.evaluate_model import evalute_model
from zenml import pipeline
@pipeline(enable_cache=True)
def pipeline(data_path="/mnt/c/Users/mahesh/Desktop/zenml_wsl/dataset/df_50k.csv",test_size=0.5):
    df=ingest_data(data_path)
    x_train,x_test,y_train,y_test=clean_df(df,test_size=test_size)
    model=train_model(x_train,y_train)
    accuracy,precision,recall,f1=evalute_model(model,x_test,y_test)
if __name__=="__main__":
    pipeline()