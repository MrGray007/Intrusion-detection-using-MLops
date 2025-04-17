import pandas as pd
import numpy as np
from zenml import step
from abc import ABC,abstractmethod
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
class DataStratagies(ABC):
    @abstractmethod
    def handle_data(self,data:pd.DataFrame):
        pass
class DataCleanStrategy(DataStratagies):
    def handle_data(self,data:pd.DataFrame):
        try:
            data=data.drop_duplicates()
            try:
                drop_columns = ['Timestamp', 'Bwd PSH Flags', 'Fwd URG Flags', 'Bwd URG Flags', 'CWE Flag Count',
                                 'Fwd Byts/b Avg', 'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg', 'Bwd Pkts/b Avg',
                                 'Bwd Blk Rate Avg']
                data=data.drop(columns=drop_columns)
            except:
                imputer=SimpleImputer(strategy='mean')
                fill_columns=['Dst Port',
                         'Protocol',
                         'Flow Duration',
                         'Tot Fwd Pkts',
                         'Tot Bwd Pkts',
                         'TotLen Fwd Pkts',
                         'TotLen Bwd Pkts',
                         'Fwd Pkt Len Max',
                         'Fwd Pkt Len Min',
                         'Fwd Pkt Len Mean',
                         'Fwd Pkt Len Std',
                         'Bwd Pkt Len Max',
                         'Bwd Pkt Len Min',
                         'Bwd Pkt Len Mean',
                         'Bwd Pkt Len Std',
                         'Flow Byts/s',
                         'Flow Pkts/s',
                         'Flow IAT Mean',
                         'Flow IAT Std',
                         'Flow IAT Max',
                         'Flow IAT Min',
                         'Fwd IAT Tot',
                         'Fwd IAT Mean',
                         'Fwd IAT Std',
                         'Fwd IAT Max',
                         'Fwd IAT Min',
                         'Bwd IAT Tot',
                         'Bwd IAT Mean',
                         'Bwd IAT Std',
                         'Bwd IAT Max',
                         'Bwd IAT Min',
                         'Fwd PSH Flags',
                         'Fwd Header Len',
                         'Bwd Header Len',
                         'Fwd Pkts/s',
                         'Bwd Pkts/s',
                         'Pkt Len Min',
                         'Pkt Len Max',
                         'Pkt Len Mean',
                         'Pkt Len Std',
                         'Pkt Len Var',
                         'FIN Flag Cnt',
                         'SYN Flag Cnt',
                         'RST Flag Cnt',
                         'PSH Flag Cnt',
                         'ACK Flag Cnt',
                         'URG Flag Cnt',
                         'ECE Flag Cnt',
                         'Down/Up Ratio',
                         'Pkt Size Avg',
                         'Fwd Seg Size Avg',
                         'Bwd Seg Size Avg',
                         'Subflow Fwd Pkts',
                         'Subflow Fwd Byts',
                         'Subflow Bwd Pkts',
                         'Subflow Bwd Byts',
                         'Init Fwd Win Byts',
                         'Init Bwd Win Byts',
                         'Fwd Act Data Pkts',
                         'Fwd Seg Size Min',
                         'Active Mean',
                         'Active Std',
                         'Active Max',
                         'Active Min',
                         'Idle Mean',
                         'Idle Std',
                         'Idle Max',
                         'Idle Min']
                data.loc[:,fill_columns]=imputer.fit_transform(data[fill_columns])
                return data
        except Exception as e:
            print(f"Error occurerd in Data {e}")
            raise e
class Normalize(DataStratagies):
    def handle_data(self,data:pd.DataFrame,exclude="Label"):
        # MinMax Normalization
        minmax = MinMaxScaler()
        data.loc[:, data.drop(columns=exclude).columns] = minmax.fit_transform(data.loc[:, data.drop(columns=exclude).columns])
        return data
class Label_encoding(DataStratagies):
    def handle_data(self,data:pd.DataFrame):
        #LAbel Encoding
        labels={'Infilteration': 5,
                 'Benign': 0,
                 'DoS': 1,
                 'DDoS': 2,
                 'Bot': 3,
                 'Brute Force': 4,
                 'DDOS': 2}
        data['Label']=data['Label'].map(labels)
        return data

class RemoveOutliers(DataStratagies):
    def outlier_capping(self,data,col):
        q1=data[col].quantile(0.25)
        q3=data[col].quantile(0.75)
        iqr=q3-q1
        upper_limit=q3+1.5*iqr
        lower_limit=q1-1.5*iqr
        data.loc[data[col]<lower_limit,col]=lower_limit
        data.loc[data[col]>upper_limit,col]=upper_limit
    def handle_data(self,data:pd.DataFrame):
        for col in data.drop('Label',axis=1).columns:
            self.outlier_capping(data=data,col=col)
        return data
class DivideDataStrategy(DataStratagies):
    def __init__(self,test_size=0.2):
        self.test_size=test_size
    def handle_data(self,data:pd.DataFrame):
        try:
            x=data.drop(columns='Label')
            y=data['Label']
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=self.test_size,train_size=1-self.test_size,random_state=69)
            return x_train,x_test,y_train,y_test
        except Exception as e:
            print(f'Error occured in Data {e}')
            raise e
class DataHandle:
    def __init__(self,data:pd.DataFrame,strategy:DataStratagies):
        self.data=data
        self.strategy=strategy
    def handle_data(self):
        try:
            if self.strategy==DivideDataStrategy():
                return self.strategy.handle_data(self.data)
            else:
                return self.strategy.handle_data(self.data)
        except Exception as e:
            print(f'Error in handling Data {e}')
            raise e

if __name__=="__main__":
    data=pd.read_csv(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv")
    clean=DataHandle(data,DataCleanStrategy())


    clean_data= clean.handle_data()
    outlier = DataHandle(clean_data, RemoveOutliers())
    df_new= outlier.handle_data()
    nor = DataHandle(df_new, Normalize())
    new_data= nor.handle_data()
    print(new_data)
    null=new_data.isnull().sum()
    print(null[null>0])
    div=DataHandle(new_data,DivideDataStrategy(test_size=0.99))
    x_train,x_test,y_train,y_test= div.handle_data()
    # print(data.shape)
    # print(data2.shape)
    import pandas as pd
    from sklearn.ensemble import VotingClassifier, AdaBoostClassifier, GradientBoostingClassifier
    from sklearn.svm import SVC
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from abc import ABC, abstractmethod

    ada_boost = AdaBoostClassifier(n_estimators=50, random_state=42)
    grad_boost = GradientBoostingClassifier(n_estimators=50, random_state=42)
    svm = SVC(probability=True, kernel='linear', random_state=42)
    log_reg = LogisticRegression(random_state=42)
    vote_class = VotingClassifier(estimators=[
        ('ada_boost', ada_boost),
        ('grad_boost', grad_boost),
        ('svm', svm),
        ('log_reg', log_reg)
    ], voting='soft')
    vote_class.fit(x_train,y_train)
    print(vote_class)



