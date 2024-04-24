# Read friends file store birth date and list of friends in dictionary
# and send happy birthday email to all those who have birthday current date
import datetime

date_format = '%Y-%m-%d'
now = datetime.date.today()
with open('./birth_date.csv') as b:
    next(b)
    for line in b:
        #print(line)
        name,b_date=line.strip().split(',')
        birth_date = b_date.strip().split('-')
        bd = datetime.date(int(birth_date[0]),int(birth_date[1]),int(birth_date[2]))
        print(bd)
        if bd.day == now.day and bd.month == now.month :
            print("Sending Mail:- ",bd)
