import logging as log
import pandas as pd
from zenml import step
from typing import Union
class Indest_data:
    def __init__(self,data_path):
        self.data_path=data_path
    def get_data(self):
        log.info('Data is been Loaded')
        return pd.read_csv(self.data_path)
@step
def ingest_data(data_path:str)->pd.DataFrame:
    try:
        ingest=Indest_data(data_path)
        data=ingest.get_data()
        return data
    except Exception as e:
        print(f'Error in data path {data_path}')
        raise e
if __name__=='__main__':
    print(ingest_data(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv"))

