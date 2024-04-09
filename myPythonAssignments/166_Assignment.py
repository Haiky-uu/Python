# 166 add some missing values in raw data in tran_dtl file (create a separate file).. Read this file,
# create a pandas dataframe and replace missing value with 1. default value, forward fill, backward fill.

import pandas as pd

dtl = pd.read_csv('./tran_dtl_.csv',names=['trans_id','Prod_id','store_id','price','date'])

df1 = pd.DataFrame(dtl)
print(df1)

FillNa = df1.fillna(1)  # Fills all Nan values with 1
print("Fill Na Normal\n",FillNa)

ForwardFillNa = df1.ffill()  # Fills na with same value as above if there is no value above then gives Nan
print("Forward fill na\n",ForwardFillNa)

BackwardFillNa = df1.bfill()  # Fills na with same value as below if there is no value below then gives Nan
print("Backward Fill na\n",BackwardFillNa)



