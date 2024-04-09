# 162 join tran_hdr, and tran_detail dataframes using pandas (try inner, outer, left outer, right outer joins)

import pandas as pd
pd.set_option('display.max_columns',9)
hdr = pd.read_csv('./tran_hdr_1_2019.csv',names=['trans_id','store_id','member_id','date'])
dtl = pd.read_csv("tran_dtl_1_2019.csv", names=['trans_id', 'product_id', 'store_id', 'price', 'date'])

print(hdr)
print(dtl)

inner = pd.merge(hdr,dtl , how='inner' ,on=['trans_id'])
print('\ninner Join \n',inner)

outer = pd.merge(hdr,dtl,how='outer',on=['trans_id','store_id'])  # or on = 'trans_id'
print('\nouter join \n ',outer)

left_outer = pd.merge(hdr,dtl, how='left', on=['trans_id','store_id'])  # or on='trans_id'
print('\n left\n',left_outer)

right_outer = pd.merge(hdr,dtl, how='right',on=['trans_id','store_id'])  # or on='trans_id'
print('\n right outer\n',right_outer)
