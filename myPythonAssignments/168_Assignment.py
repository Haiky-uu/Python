# 168 read product data and tran_dtl data from mySQL to pandas dataframe. Join two data frames

import pandas as pd
import mysql.connector

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

t_dtl = pd.DataFrame(dtl,columns=['trans_id','prod_id','store_id','price','date'])
# print(t_dtl)


cursor.reset()

cursor.execute("SELECT * FROM product")
pro = cursor.fetchall()


#for _ in pro:
#    print(_)

p_pro = pd.DataFrame(pro,columns=['prod_id','description','price','category','qty'])
#print(p_pro)

pd.set_option("display.max_columns",10)
pd.set_option("display.min_rows",100)
join = pd.merge(t_dtl,p_pro, on='prod_id', how='inner')
print("After Joining\n",join)

cursor.close()
conn.commit()
conn.close()

