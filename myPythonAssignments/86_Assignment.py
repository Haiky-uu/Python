# 86 write a function to find factors of a number and add them in list

def factors(num: int, fact: list):
    for i in range(1, num+1):
       # print(i)
        if (num % i == 0):
            print(f'Factors of {num} is',i)
            fact.append(i)


num = int(input("Enter a number: "))
fact = []

factors(num, fact)
print(fact)
