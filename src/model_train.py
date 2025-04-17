import pandas as pd
from sklearn.ensemble import VotingClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from abc import ABC ,abstractmethod
from sklearn.base import ClassifierMixin

ada_boost = AdaBoostClassifier(n_estimators=50, random_state=42)
grad_boost = GradientBoostingClassifier(n_estimators=50, random_state=42)
svm = SVC(probability=True, kernel='linear', random_state=42)
log_reg = LogisticRegression(random_state=42)

class Model(ABC):
    @abstractmethod
    def train(self,x_train:pd.DataFrame,y_train:pd.DataFrame):
        pass

class Votingclassifier(Model):
    def train(self,x_train:pd.DataFrame,y_train:pd.DataFrame)->ClassifierMixin:

        vote_class=VotingClassifier(estimators=[
                            ('ada_boost', ada_boost),
                            ('grad_boost', grad_boost),
                            ('svm', svm),
                            ('log_reg', log_reg)
                        ], voting='soft')
        vote_class.fit(x_train,y_train)
        return vote_class
class RandomForest(Model):
    def train(self,x_train:pd.DataFrame,y_train:pd.DataFrame):
        random_forest=RandomForestClassifier()
        random_forest.fit(x_train,y_train)
        return random_forest
if __name__=="__main__":
    from src.clean import DivideDataStrategy,DataHandle,Label_encoding,RemoveOutliers,Normalize,DataCleanStrategy
    data=pd.read_csv(r"C:\Users\mahesh\Desktop\zen\dataset\df_50k.csv")
    clean=DataHandle(data,DataCleanStrategy())
    clean_data= clean.handle_data()
    outlier = DataHandle(data, RemoveOutliers())
    df_new= outlier.handle_data()
    nor = DataHandle(df_new, Normalize())
    new_data= nor.handle_data()
#     # encoding = DataHandle(new_data, Label_encoding())
#     # data=encoding.handle_data()
    div=DataHandle(new_data,DivideDataStrategy(test_size=0.9))
    x_train,x_test,y_train,y_test= div.handle_data()
    print(x_test.shape)
    # print(x_test)
    model=Votingclassifier()
    model=model.train(x_train,y_train)
    print(model)
    print(model.predict(x_train))

