# 157 add a new hard coded column with value = "TEST" to tran_hdr dataframe

import pandas as pd

file = pd.read_csv('./tran_hdr_1_2019.csv')

df1 = pd.DataFrame(file)
print("Initial Dataframe:\n",df1)

df1['New_col'] = "Test"
print("After\n",df1)