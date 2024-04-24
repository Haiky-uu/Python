# 170 calculate rolling 3 months sale (current and two previous) by product, year and month
import datetime

import pandas as pd
import mysql.connector
from datetime import date
from dateutil.relativedelta import relativedelta


curr_date = date.today()
end_date = curr_date - relativedelta(months=3)

print(curr_date)
print(end_date)

conn = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '258925',
    database = 'Retail_pro'
)

if conn.is_connected():
    print('yay')

pd.set_option('display.max_columns',None)
pd.set_option('display.min_rows',20)

cursor = conn.cursor()
cursor.execute('Select * from trans_dtl where trans_date >= %s',(end_date,))
t_dtl = cursor.fetchall()
# print(t_dtl)
df_t_dtl = pd.DataFrame(t_dtl, columns=['trans_id','prod_id','store_id','amount','date'])

cursor.reset()

cursor.execute('Select * from product')
p_pro = cursor.fetchall()
# print(p_pro)
df_p_pro = pd.DataFrame(p_pro, columns=['prod_id','description','price','category','qty'])

dtl_pro = pd.merge(df_t_dtl,df_p_pro, how='inner', on='prod_id')
# print(dtl_pro.dtypes)
dtl_pro['date'] = pd.to_datetime(dtl_pro['date'])
# print(dtl_pro.dtypes)

dtl_pro['year'] = dtl_pro['date'].dt.year
dtl_pro['month'] = dtl_pro['date'].dt.month

# print(dtl_pro)
total_sum = dtl_pro.groupby(['description','year','month'])['amount'].sum().reset_index()

# print(df_t_dtl)
# print(df_p_pro)
print(total_sum)

cursor.close()
conn.commit()
conn.close()
