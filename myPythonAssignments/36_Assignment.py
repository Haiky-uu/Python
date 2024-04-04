# 36 get a number from user and check if the number is perfect square.
def perfectsquare(num):
    for i in range(1, num):
        if (i * i == num):
            #return True
            print("perfect square")
        elif (i * i > num):
            print("Not a perfect square")
perfectsquare(4)
