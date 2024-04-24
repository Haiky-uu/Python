# 165 Read jason file in pandas

import pandas as pd


pd.set_option('Display.max_columns',None)
pd.set_option('Display.min_rows',None)
df1 = pd.read_json('./json2.json')
print(df1)
