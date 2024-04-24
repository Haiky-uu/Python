# 38 Read product file and tran_dtl file and implement inner join using loops
# (use two for loops) -- implement left, right and full outer join


def left_join():
    print("Left Join ------")
    dtl = set()
    for line in open('./tran_dtl_.csv'):
        print(line)
        trans_id, prod_id, qty, amount, date = line.strip().split(',')
        dtl.add(prod_id)
        for line2 in open('./product.csv'):
            prodID, desc, price, cat, qty = line2.strip().split(',')
            if prodID in dtl:
                print(trans_id,prod_id,qty,amount,date,prodID,desc,price,cat,qty)
            else:
                print(trans_id,prod_id,qty,amount,date,'N/A','N/A','N/A','N/A','N/A')

def right_join():
    dtl = set()
    for line in open('./tran_dtl_.csv'):
        #print(line)
        trans_id, prod_id, qty, amount, date = line.strip().split(',')
        dtl.add(prod_id)
        for line2 in open('./product.csv'):
            print(line2)
            prodId,desc, price, cat, qty = line2.strip().split(',')
            if prodId in dtl:
                print(trans_id, prod_id, qty, amount, date,prodId, desc, price, cat, qty)
            else:
                print('N.A','N.A','N.A','N.A',prodId,desc,price,cat,qty)
def outer_join():
    dtl = set()
    for line in open('./tran_dtl_.csv'):
        # print(line)
        trans_id, prod_id, qty, amount, date = line.strip().split(',')
        dtl.add(prod_id)
        for line2 in open('./product.csv'):
            print(line2)
            prodId,desc, price, cat, qty = line2.strip().split(',')
            if prodId not in dtl:
                print('N.A','N.A','N.A','N.A','N.A', prodId, desc, price, cat, qty)


def main():
    right_join()
    left_join()
    outer_join()

if __name__ == "__main__":
    main()

