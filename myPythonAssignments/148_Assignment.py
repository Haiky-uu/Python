# 148 Write a program to read total sale by member by product for last 12 months
# (use SQL to get agg data) in pandas dataframe, find max sale product for every
# member, min sale product for every member and write it to two separate files
# (1. sale by member, by product. 2. min and max sale and product by member)

import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='258925',
    database='Retail_pro'
)

cursor = conn.cursor()

cursor.execute('''SELECT member_id , product_id ,ROUND(SUM(td.amount),2) as total_trans  FROM trans_hdr th
JOIN trans_dtl td ON th.trans_id = td.trans_id 
WHERE td.trans_date > DATE_SUB(NOW(), INTERVAL 1 YEAR) 
GROUP BY member_id, product_id ;''')


query = cursor.fetchall()

df1 = pd.DataFrame(query,columns=['member_id','product_id','total_trans'])

df1.to_csv('./sale_by_member_by_product.csv')

print(df1)

max_total = df1.groupby('member_id')['total_trans'].max().reset_index()
max_total = max_total.rename(columns={'total_trans':'max_product_sale'})

min_total = df1.groupby('member_id')['total_trans'].min().reset_index()
min_total = min_total.rename(columns={'total_trans':'min_product_sale'})

merged = pd.concat([max_total,min_total],axis=1)
print(merged)

with open('./max_min_member_product_sale.csv','w') as f:
    pd.concat([max_total,min_total],axis=1).to_csv(f,index=False)

#print(max_total)
#print(min_total)
cursor.close()
conn.commit()
conn.close()
