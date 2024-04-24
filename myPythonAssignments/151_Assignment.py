# 151 Write a program to get today's date or user input date, read rolling 12-month data
# from SQL (tran_dtl table and tran_hdr table) in pandas dataframe, aggregate by member,
# by product and normalize data to get score for every product for every member.

import datetime
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password='258925',
    database='Retail_pro'
)

cursor = conn.cursor()
today = datetime.date.today()
roll = today - datetime.timedelta(365 * 1)
print(roll)


cursor.execute("SELECT * FROM trans_hdr WHERE trans_date >= %s", (roll,))

hdr = cursor.fetchall()
hdr_df = pd.DataFrame(hdr,columns=['trans_id','member_id','store_id','date'])

cursor.reset()

cursor.execute("SELECT * FROM trans_dtl WHERE trans_date >= %s", (roll,))

dtl = cursor.fetchall()
dtl_df = pd.DataFrame(dtl,columns=['trans_id','product_id','qty','amount','date'])

print(hdr_df)
print(dtl_df)

merged = pd.merge(hdr_df,dtl_df, how='inner' , on='trans_id')
print(merged)

agg = merged.groupby(['member_id','product_id']).agg({'qty': 'sum', 'amount': 'sum'}).reset_index()
agg['score'] = agg['amount'] / agg['qty']

print(agg)

cursor.close()
conn.commit()
conn.close()


