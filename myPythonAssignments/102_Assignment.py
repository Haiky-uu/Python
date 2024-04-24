# 102 read file containing details of professionals (doctor, engineer, etc.). Implement OOP solution
# and check polymorphism (see if correct method is getting called)

cnt = 0
dic = {}

class Doctor:
    def __init__(self, person, f_name, l_name, age, gender, speciality, salary):
        self.person = person
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.speciality = speciality
        self.salary = salary

    def print_details(self):
        print("Person : " ,self.person,"Full Name : ",self.f_name+' '+self.l_name,"Speciality: ",self.speciality,"Salary: ",self.salary)


class Employee:

    def __init__(self, person, f_name, l_name, age, gender, speciality, salary):
        self.person = person
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.speciality = speciality
        self.salary = salary

    def print_details(self):
        print("Person : ", self.person, "Full Name : ", self.f_name +' '+ self.l_name, "Speciality: ", self.speciality,"Salary: ", self.salary)


class Teacher:

    def __init__(self, person, f_name, l_name, age, gender, speciality, salary):
        self.person = person
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.speciality = speciality
        self.salary = salary

    def print_details(self):
        print("Person : ", self.person, "Full Name : ", self.f_name+' '+ self.l_name, "Speciality: ", self.speciality,"Salary: ", self.salary)


ls = []
with open('./polymorp.csv') as f:
    for line in f:
        if cnt==0:
            cnt+=1
            continue
        person,f_name,l_name,age,gender,speciality,salary = line.strip().split(',')
        if person == 'Doctor':
            d1 = Doctor(person,f_name,l_name,age,gender,speciality,salary)
            ls.append(d1)

        if person == 'Engineer':
            e1 = Employee(person,f_name,l_name,age,gender,speciality,salary)
            ls.append(e1)

        if person == 'Teacher':
            t1 = Teacher(person,f_name,l_name,age,gender,speciality,salary)
            ls.append(t1)
    #print(ls)

for obj in ls:
    print(obj.print_details())
