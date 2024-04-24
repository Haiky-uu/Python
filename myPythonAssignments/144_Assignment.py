# 144 Write a program to read data from Product table on
# mysql and write it to a csv file

import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '258925',
    database = 'retail'
)

if conn.is_connected():
    print('yay')

cursor = conn.cursor()

cursor.execute("Select * from product")
prd_d = cursor.fetchall()
print(prd_d)

pro = pd.DataFrame(prd_d,columns=['prod_id','description','price','category','qty'])

#print(pro)

pro.to_csv('./product.csv',index=False)