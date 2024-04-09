# 161 find profile of numerical variable (min, max, quantile, mean, median, standard deviation) using pandas

import pandas as pd

file = pd.read_csv('tran_dtl_1_2019.csv')

df1 = pd.DataFrame(file)

print(df1.describe())
