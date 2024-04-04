# 37 Read product file and tran_dtl file and implement inner
# join using loops (use two for loops)

desDict = {}
cnt =0
for line in open('./tran_dtl.csv'):
    print(line)
    if cnt == 0:
        cnt+=1
        continue
    trans_id, p_id, qty, price, date = line.strip().split(',')
    pid = int(p_id)
    desDict[p_id]= [trans_id,qty,price,date]

print(desDict)


cnt = 0
for line in open('./product.csv'):
    if cnt == 0:
        cnt+=1
        continue
    product_id, description, price, category, max_qty = line.strip().split(',')
    product_id = int(product_id)

    for product_id in desDict:
        print(f{p})