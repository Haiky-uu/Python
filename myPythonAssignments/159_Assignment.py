# 159 filter tran_dtl_dataframe  on qty > 4

import pandas as pd

f = pd.read_csv('./tran_dtl_1_2019.csv')
f.columns = ['trans_id','prod_id','qty','price','date']
df1 = pd.DataFrame(f)

print(df1)

df2 = df1[df1['qty']>4]
print('\nAfter\n',df2)

