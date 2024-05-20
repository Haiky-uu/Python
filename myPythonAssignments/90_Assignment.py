# 90 Write a program to get fibonaci number of given number

def fibo(n: int) -> int:
   if n == 1:
       return 1

   if n == 0:
       return 0

   return fibo(n-1) + fibo(n-2)


n = 5
print(fibo(n))