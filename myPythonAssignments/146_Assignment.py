# 146 Write a program to read data from product table on mysql and find number of products by category and
# insert this data in SQL table category_num_products

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='258925',
    database='retail'
)

cursor = conn.cursor()

cursor.execute('Select * from product')

pro = cursor.fetchall()

cursor.reset()


cat_num_prod = ('CREATE TABLE cat_num_prod('
                'category VARCHAR(30),'
                'no_of_prod INT'
                ');')

cursor.execute("DROP TABLE IF EXISTS cat_num_prod")

cursor.execute(cat_num_prod)

pro_cat = ("""
INSERT INTO cat_num_prod
SELECT category ,COUNT(product_id)  FROM  product p GROUP BY category;""")

cursor.execute(pro_cat)

cursor.close()
conn.commit()
conn.close()
