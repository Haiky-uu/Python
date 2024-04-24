# 79  write a program to add two number a and b and return output as c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add(x,y):
    c = x + y
    print("C: ",c)

def main():
    add(a,b)

if __name__ == '__main__':
    main()
