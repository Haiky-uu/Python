# 167 read same file from 166, create pandas dataframe and replace missing values with separate values for each column.

import pandas as pd

file = pd.read_csv('./tran_dtl_.csv',names=['trans_id','prod_id','store_id','price','date'])

df1 = pd.DataFrame(file)

print(df1)

fill = df1.fillna({'prod_id':2,'store_id':4,'price':7})
print(fill)


# Filling by rows or index's
fill_values = {
    1:{'prod_id':4,'store_id':8,'price':9},
    3:{'prod_id':3,'store_id':5,'price':6}
}

for key,value in fill_values.items():
    df1.loc[key]=df1.loc[key].fillna(value)
print("by values\n",df1)