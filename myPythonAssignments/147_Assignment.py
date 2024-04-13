# 147 Write a program to read data from transaction table on mysql as pandas data frame,
# find aggregate monthly sale (in pandas) and write it to csv and SQL Table (monthly_sale)
import csv

import pandas as pd
import mysql.connector
import datetime

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='258925',
    database='retail'

)

cursor = conn.cursor()
cursor.execute('Select * from tran_dtl')

dtl = cursor.fetchall()
dtl_df = pd.DataFrame(dtl,columns=['tran_id','prod_id','store_id','amount','date'])

dtl_df['date'] = pd.to_datetime(dtl_df['date'])
dtl_df['month'] = dtl_df['date'].dt.month

print(dtl_df)

total_sale_month = dtl_df.groupby(['month'])['tran_id'].count().reset_index()
total_sale_month = total_sale_month.rename(columns={'tran_id':'total_tran_monthly'})
print(total_sale_month)

total_sale_month.to_csv('./total_tran_monthly.csv', index=None)

cursor.reset()

cursor.execute('DROP TABLE IF EXISTS monthly_sale;')
cursor.execute("CREATE TABLE monthly_sale("
               "month INT,"
               "total_tran INT);")

f = csv.reader(open('./total_tran_monthly.csv'))
next(f)
for line in f:
    # print(line)
        # month, total_trans = line.strip().split(',')
    cursor.execute("INSERT INTO monthly_sale VALUES(%s,%s); ",line)

'''
Without using import csv
with open('./total_tran_monthly.csv') as f:
    next(f)  # Skip the header line
    for line in f:
        month, total_tran = line.strip().split(',')
        cursor.execute("INSERT INTO monthly_sale (month, total_tran) VALUES (%s, %s);", (month, total_tran))
'''
cursor.close()
conn.commit()
conn.close()


