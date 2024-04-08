# 163 join tran_hdr and tran_detail dataframes using join conditions on two columns tran_id and tran_dt

import pandas as pd

pd.set_option('display.max_columns', 9)
hdr = pd.read_csv('./tran_hdr_1_2019.csv',names=['trans_id','store_id','member_id','trans_dt'])
dtl = pd.read_csv('./tran_dtl_1_2019.csv' , names=['trans_id','product_id','store_id','price','trans_dt'])

join = pd.merge(hdr,dtl, on = ['trans_id','trans_dt'])
print(join)