# 72 read product file and tran_dtl file. Store product file in dictionary and implement
# inner, left, right and full outer join. -- take join option as command line argument


def insertDict():
    prod = {}
    cnt = 1
    for line in open('./product.csv'):
        if cnt == 1:
            cnt += 1
            continue
    #print(line)
        prod_id, desc, price, cat, qty = line.strip().split(',')
        prod[prod_id] = [desc,price,cat,qty]

    #print(prod)
    return prod


def inner(prod):
    cnt = 0
    for line in open('./tran_dtl.csv'):
        if cnt == 0:
            cnt += 1
            continue
        tran_id, prod_id, qty, price, date = line.strip().split(',')
        for k,v in prod.items():
            if k == prod_id:
                print(v[0],',',v[1],',',v[2],',',v[3],',',tran_id,',',prod_id,',',qty,',',price,',',date)


def left(prod):
    cnt = 0
    for line in open('./tran_dtl.csv'):
        if cnt == 0:
            cnt += 1
            continue
        tran_id, prod_id, qty, price, date = line.strip().split(',')
        if prod_id in prod.keys():
           v = prod[prod_id]
           print(v[0], ',', v[1], ',', v[2], ',', v[3], ',', tran_id, ',', prod_id, ',', qty, ',', price, ',',date)
        else:
           print('N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A',',', tran_id, ',', prod_id, ',', qty, ',', price, ',',date)


def right(prod):
    cnt = 0
    for line in open('./tran_dtl.csv'):
        if cnt == 0:
            cnt += 1
            continue
        tran_id, prod_id, qty, price, date = line.strip().split(',')
        if prod_id in prod.keys():
            v = prod[prod_id]
            print(v[0], ',', v[1], ',', v[2], ',', v[3], ',', tran_id, ',', prod_id, ',', qty, ',', price, ',',date)
        else:
            print(v[0], ',', v[1], ',', v[2], ',', v[3] ,',','N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A',',','N.A')

def outer(prod):
    cnt = 0
    for line in open('./tran_dtl.csv'):
        if cnt == 0:
            cnt += 1
            continue
        tran_id, prod_id, qty, price, date = line.strip().split(',')
        if prod_id in prod.keys():
            v = prod[prod_id]
            print(v[0], ',', v[1], ',', v[2], ',', v[3], ',', tran_id, ',', prod_id, ',', qty, ',', price, ',', date)
        else:
            print('N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A', ',', 'N.A')

def main():
    print("Program")
    user = input("Enter join to use: ")
    prod = insertDict()
    if user == 'inner':
        inner(prod)
    elif user == 'left':
        left(prod)
    elif user == 'right':
        right(prod)
    elif user == 'outer':
        outer(prod)

if __name__ == '__main__':
    main()

