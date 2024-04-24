# 152 Write a program to get today's date or user input date, read rolling 12 month data from SQL
# (tran_dtl table and tran_hdr table)
# in pandas dataframe, read product table in pandas data frame. Calculate score for every category for every member.
import datetime
import pandas as pd
import mysql.connector

pd.set_option('display.max_columns',None)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='258925',
    database='Retail_pro'
)

today_date = datetime.date.today()
roll = today_date - datetime.timedelta(365 * 1)

cursor = conn.cursor()

cursor.execute("Select * from trans_hdr where trans_date >= %s ",(roll,))

hdr = cursor.fetchall()
hdr_df = pd.DataFrame(hdr,columns=['trans_id','member_id','store_id','date'])

cursor.reset()

cursor.execute("Select * from trans_dtl where trans_date >= %s",(roll,),)

dtl = cursor.fetchall()
dtl_df = pd.DataFrame(dtl,columns=['trans_id','prod_id','qty','amount','date'])

cursor.reset()

cursor.execute("Select * from product;")

pro = cursor.fetchall()
pro_df = pd.DataFrame(pro,columns=['prod_id','description','price','category','qty_p'])

merge = pd.merge(hdr_df,dtl_df, how='inner',on='trans_id')

proMerge = pd.merge(merge,pro_df , how='inner',on='prod_id')
print(proMerge)

calculate = proMerge.groupby(['member_id','category']).agg({'qty':'sum','amount':'sum'}).reset_index()
calculate['score'] = calculate['amount'] / calculate['qty']
print(calculate)

