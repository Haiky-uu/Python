# 70 read file user-pwd, store data in list.
# Ask user to enter username and pwd and check if he/she is a valid user

dic = {}
def extract():
    for a in open("./user-pwd.py"):
        b,c = a.strip().split(':')
        dic[b] = c
    return dic

def program(dic):
    user = input("Enter username: ")
    passw = input("Enter password: ")
    #print(dic)
    if user in dic:
        if passw == dic[user]:
            print("valid user")
        else:
            print('invalid')
    else:
        print('invalid')
def main():
   dic = extract()
   program(dic)

if __name__ == '__main__':
    main()

