import logging as log
import pandas as pd
from src.clean import DataCleanStrategy,DataHandle,DivideDataStrategy,RemoveOutliers,Normalize
from zenml import step
from typing import Tuple
from typing_extensions import Annotated
@step
def clean_df(df:pd.DataFrame,test_size: float=0.2)-> Tuple[
    Annotated[pd.DataFrame,'x_train'],
    Annotated[pd.DataFrame,'x_test'],
    Annotated[pd.Series,'y_train'],
    Annotated[pd.Series,'y_test']
]:
    try:
        clean_data=DataHandle(df,DataCleanStrategy())
        cleaned_df= clean_data.handle_data()
        outliers_remove=DataHandle(cleaned_df,RemoveOutliers())
        df_outlier= outliers_remove.handle_data()
        normalizer=DataHandle(df_outlier,Normalize())
        df= normalizer.handle_data()
        data_splitter=DataHandle(df,DivideDataStrategy(test_size))
        x_train,x_test,y_train,y_test= data_splitter.handle_data()
        return x_train,x_test,y_train,y_test
    except Exception as e:
        log.error("Error in Cleaning Data")
        raise e

if __name__=="__main__":
    df=pd.read_csv(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv")
    # clean_data = DataHandle(df, DataCleanStrategy())
    # cleaned_df = clean_data.handle_data()
    # outliers_remove = DataHandle(cleaned_df, RemoveOutliers())
    # df_outlier = outliers_remove.handle_data()
    # normalizer = DataHandle(df_outlier, Normalize())
    # df = normalizer.handle_data()
    # print(df['Label'])
    x_train,x_test,y_train,y_test=clean_df(df)
    print(y_test)