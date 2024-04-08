# Read transaction_hdr file and convert it into pandas dataframe.
# Print top 10 and bottom 10 records (head and tail) to see sample data.

import pandas as pd

f = pd.read_csv('./tran_hdr_1_2019.csv')

df1 = pd.DataFrame(f)
# print(df1)
print("Head:- ",'\n',df1.head(n =10),'\n')
print("Tail:-",'\n',df1.tail(n = 10))