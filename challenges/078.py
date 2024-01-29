tvTitles = ['BigBangTheory', 'TheGoodDoctor', 'Asur', 'TheMentalist']

for title in tvTitles:
    print(title)

user = input("Enter a show you ant to insert: ")
pos = int(input("Enter the position you want it to enter: "))
tvTitles.insert(pos, user)
print(tvTitles)

