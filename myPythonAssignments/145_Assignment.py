# 145 Write a program to read data from product table on mysql
# and find number of products by category and write it to csv.

import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='258925',
    database='retail'
)

if conn.is_connected():
    print('yay')

cursor = conn.cursor()

cursor.execute("Select * from product")
pro_d = cursor.fetchall()

pro_df = pd.DataFrame(pro_d,columns=['pro_id','desc','price','category','qty'])

prod = pro_df.groupby(by='category')['pro_id'].count().reset_index()

prod = prod.rename(columns={'category':'category','pro_id':'no_of_products'})
print(prod)

prod.to_csv('./category_by_product.csv',index=None)