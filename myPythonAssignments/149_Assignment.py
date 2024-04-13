# 149 Write a program to read product data from SQL in python program save it
# in dict (save id as key and object as value). Take user input for product description
# and find if product exists and if it exists then display product details.

import mysql.connector

def conne():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='258925',
        database='retail'
    )
    cursor = conn.cursor()
    cursor.execute('Select * from product;')
    query = cursor.fetchall()
    return query

def dictt(query):
    pro_des = {}
    for line in query:
        pro_id, description,price,cat,qty = line
        # print(pro_id,description,price,cat,qty)
        pro_des[description] = [pro_id,price,cat,qty]

    print(pro_des)
    return pro_des

def find(pro_des):
    desc = input("Enter product description: ")

    for key,value in pro_des.items():
        if key == desc:
            p_id,priceA,cata,q = value
            print("Product_id: ",p_id)
            print("Price: ",priceA)
            print("Category: ",cata)
            print("Quantity: ",q)
            break
    else:
        print("Product Not found!")


def main():
    query = conne()
    pro_des = dictt(query)
    find(pro_des)

    
if __name__ == '__main__':
    main()

