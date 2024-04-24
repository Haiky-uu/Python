# 37 Read product file and tran_dtl file and implement inner
# join using loops (use two for loops)

cnt =0
cnt2 = 0
for line in open('./tran_dtl.csv'):
    if cnt == 0:
        cnt+=1
        continue
    trans_id, p_id, qty, amt, date = line.strip().split(',')
    for line2 in open('./product.csv'):
        if cnt2 == 0:
            cnt2 += 1
            continue
        # print(line2)
        prod_id,desc,price,cat,qty = line2.strip().split(',')
        #print(p_id)
        #print(prod_id)
        if (p_id == prod_id):
            #with open('./temp.csv','a') as f:
                #f.write(trans_id+','+p_id+','+qty+','+amt+','+desc+','+cat+','+date+'\n')
                print(trans_id+','+p_id+','+qty+','+amt+','+desc+','+cat+','+date)
    #f.close()

