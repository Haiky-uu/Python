# read transaction_hdr file with or without header, read without
# header and assign columns as given in config file

import pandas as pd
from conf2 import header as hd


f = pd.read_csv('./tran_hdr_1_2019.csv',header=None)
#or f = pd.read_csv('./tran_hdr_1_2019.csv',header=None,names=hd)

f.columns = hd

print(f)


