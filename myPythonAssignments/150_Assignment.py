# 150 Write a program to read product data from SQL in python program save it in dict
# (save category as key and list of objects related to that category as value).
# Take user input for category and display all product options in that category.

import mysql.connector

conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '258925',
        database = 'retail'
)

cursor = conn.cursor()
cursor.execute("Select * from product")
pro = cursor.fetchall()
print(pro)
pro_dict = {}
for line in pro:
    pro_id, description, price, category, qty = line

    if category in pro_dict:
        pro_dict[category].append((pro_id,description,price,qty))
    else:
        pro_dict[category] = [(pro_id,description,price,qty)]
print(pro_dict)

cat = input("Enter a category: ")
count = 0
for key,val in pro_dict.items():
    for values in val:
       prod_id, name, price, qty = values
       if cat == key:
           print("----------")
           print("Product_id: ",prod_id)
           print("Product_name: ",name)
           print("Price: ",price)
           print("qty: ",qty)
           count+=1
           print(f"No of products {key} have {count}")




