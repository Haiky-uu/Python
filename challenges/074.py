colors = ['Red', 'Orange', 'Green', 'Black', 'White', 'Blue', 'Purple', 'Yellow', 'Pink', 'Brown']

user = input("Enter number between 0 to 4 starting and between 5 to 9 ending: ")

start, end = user.strip().split(" ")
start = int(start)
end = int(end)

print(colors[start:end])

'''
for color in colors:
    print(colors.index(start), colors.index(end))
    break
'''