from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd


class dropcol(BaseEstimator, TransformerMixin):
    def __init__(self, columns_drop):
        self.columns_drop = columns_drop

    def fit(self, x, y=None):
        return self

    def transform(self, x):
        try:
            xx = x.drop(self.columns_drop, axis=1)
            # print('yes')

            return xx
        except Exception as e:
            print(e)
            return x


# cutom Transformer 2
class to_numeric(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self

    def transform(self, x):
        for i in x.columns:
            x[i] = pd.to_numeric(x[i], errors='coerce')
        for i in x.columns:
            if x[np.isinf(x[i])].shape[0] >= 1:
                x.loc[np.isinf(x[i]), i] = np.nan
        return x
