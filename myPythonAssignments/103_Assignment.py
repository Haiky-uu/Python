# 103 read grocery file, create instance of grocery class for every line, store it in
# dictionary with grocery name as key. Ask user to enter grocery name and quantity and
# calculate total amount for user grocery purchase.
import pandas as pd


class Grocery:
    def __init__(self,p_id,p_name,p_price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price


def insert(file):
    with open(file) as f:
        grocery = {}
        for line in f:
            p_id,p_pro,p_amt = line.strip().split(',')
            p_id = int(p_id)
            p_amt = int(p_amt)
            obj = Grocery(p_id,p_pro,p_amt)
            grocery[p_pro] = obj
        return grocery


def calculate(grocery):

    pur = input("Lets purchase y/n: ")
    total = 0
    grow = {'item':[],'qty':[],'price':[],'total_val':[]}
    while pur == 'y':

        user = input("Enter name of product to purchase: ")
        for k, v in grocery.items():
            if user == k:
                qty = int(input("Enter qty of product to purchase: "))
                val = v.p_price*qty
                total += val
                grow['item'].append(user)
                grow['qty'].append(qty)
                grow['price'].append(v.p_price)
                grow['total_val'].append(val)
                break
        pur = input("Do you want to purchase more(y/n): ")

    else:
        print("Bye")
    print("________#########___________")
    print("Your items are: ")
    grocery = pd.DataFrame(grow)
    print(grocery)
    print("Your total grocery value is : ", total)