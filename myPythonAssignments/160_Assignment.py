# 160 read tran_detail file, create pandas data frame and do slicing and dicing (select only partial columns and rows)

import pandas as pd

file = pd.read_csv('tran_dtl_1_2019.csv', names=['trans_id', 'product_id', 'qty', 'price', 'date'])

df1 = pd.DataFrame(file)
print(df1[2:5])   # Slicing selecting only partial rows

print("Abc")
print(df1.loc[:,['product_id','qty']])  # Slicing all rows of 2 columns only
print(df1.loc[10,['trans_id','product_id','qty']])  # slicing only row no 10 of partial columns
print(df1.loc[5:,['trans_id','product_id','qty']])  # slicing all rows starting from row 5 to end with partial columns
print(df1.loc[15:25,['trans_id','product_id','date']])  # slicing rows starting from row 15 to 25 with partial columns
print(df1.loc[0,'trans_id'])  # Getting a scalar value i.e single value
print(df1.iat[1,2])


print(df1.iloc[3:6, 0:2])  # getting rows (3,4,5) and (0,1)
print(df1.iloc[[3, 4, 5], [0, 1]])  # same as above

print(df1.iloc[1:3, :])  # selected rows and all columns
print(df1.iloc[:, 1:3])  # All rows and selected columns

print(df1.iloc[1, 2])  # Scalar




