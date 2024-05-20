# Get two variables for user N and R and write a program to generate all possible combinations N C R

def fact(num: int) -> int:

    if num == 1:
        return 1

    if num == 0:
        return 0

    if num < 0:
        print("Negative number")

    return num * fact(num-1)


print(fact(12))


def ncr(n: int,r: int) -> float:
    a = fact(n)
    b = fact(r)
    c = fact(n-r)
    return a/(b*c)



n = 4
r = 2
f = n-r
print(ncr(n,r))



