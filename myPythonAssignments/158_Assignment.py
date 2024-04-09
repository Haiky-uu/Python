# 158 add new column to tran_detl dataframe ==> new column is "price" = sales_amt/qty

import pandas as pd

file = pd.read_csv('tran_dtl_1_2019.csv', names=['trans_id', 'prod_id', 'qty', 'sale_amt', 'date'])

df1 = pd.DataFrame(file)
print(df1)
df1['price'] = df1['sale_amt']/df1['qty']
print("After\n ",df1)