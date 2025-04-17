import pandas as pd
import numpy as np
from zenml import step,pipeline
from typing_extensions import Annotated
from typing import Tuple
@step
def read(add):
    return pd.read_csv(add)
@step
def clean(df:pd.DataFrame)-> pd.DataFrame:
    df_=df.drop(columns=['Dst Port','Protocol','Flow Duration'])
    return df_
@pipeline
def pipelines(path):
    df=read(path)
    clean(df)

pipelines(r"C:\Users\mahesh\Downloads\test(400).csv")