# 156 read transaction_hdr(1_jan_2019) data and convert it into pandas dataframe
# , similarly read transaction_dtl_data (1_jan_2019)

import pandas as pd

file = pd.read_csv('./tran_hdr_1_2019.csv')

df1 = pd.DataFrame(file)
print("trans_hdr_data_frame\n",df1)

file2 = pd.read_csv('tran_dtl_1_2019.csv')

df2 = pd.DataFrame(file2)
print("trans_dtl_data_frame\n",df2)
