subjects = ['English', 'Maths', 'Science', 'History', 'Geography', 'Civics']

user = input("Which subject you want to remove: ")

if (user in subjects):
    subjects.remove(user)
    print("Your subject is removed.")
    print(sorted(subjects))
else:
    print('Invalid Input!')
