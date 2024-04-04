def getb(min: int,max: int,bucket: int,bucketList: list):
    intercept = max - min
    bucketList.append(min)
    while(intercept>bucket):
        min+=bucket
        bucketList.append(min)
        intercept = max-min
    bucketList.append(max)
bktDict = {}

with open('./casewhen.csv') as f:
    cnt = 0
    for line in f:
        if cnt == 0:
            cnt += 1
            continue
        print(line)
        cal,mn_val,mx_val,bucket_size=line.strip().split(',')
        mn_val = int(mn_val)
        mx_val = int(mx_val)
        bucket_size = int(bucket_size)
        bucketList = []
        getb(mn_val,mx_val,bucket_size,bucketList)
        print(bucketList)
        bktDict[cal]=bucketList
        print(bktDict)



