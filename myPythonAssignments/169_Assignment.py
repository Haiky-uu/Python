# 169 calculate total sales by year, month and product description (use dataframe prepared in previous assignment)

import pandas as pd
import mysql.connector
import datetime as dt

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='258925',
    database='retail'
)

if conn.is_connected():
    print('yay')

cursor = conn.cursor()

cursor.execute("SELECT * FROM tran_dtl")

dtl = cursor.fetchall()
# print(dtl)
#for _ in dtl:
#    print(_)

t_dtl = pd.DataFrame(dtl,columns=['trans_id','prod_id','store_id','amount','date'])
# print(t_dtl)

cursor.reset()

cursor.execute("SELECT * FROM product")
pro = cursor.fetchall()


#for _ in pro:
#    print(_)

p_pro = pd.DataFrame(pro,columns=['prod_id','description','price','category','qty'])
#print(p_pro)

pd.set_option("display.max_columns",None)
pd.set_option("display.min_rows",10)
dtl_pro = pd.merge(t_dtl,p_pro, on='prod_id', how='inner')
#print("After Joining\n",join)


dtl_pro['date'] = pd.to_datetime(dtl_pro['date'])  # It was object in sql now it gets converted to datetime

dtl_pro['year']= dtl_pro['date'].dt.year  # extracted year and month from date
dtl_pro['month']= dtl_pro['date'].dt.month

total_sale = dtl_pro.groupby(['year','month','description'])['amount'].sum().reset_index()

print(total_sale)

print(dtl_pro.dtypes)



# total_sale = tr

print(dtl_pro)

cursor.close()
conn.commit()
conn.close()


