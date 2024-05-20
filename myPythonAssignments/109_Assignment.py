# 109 read employee manager file build employee class and define class variable employee count and check
# working of class variable

class Employee:

    emp_count = 0

    def __init__(self,emp_id, emp_name, age, height, sal, man_id):
        self.emp_id = emp_id
        self.name = emp_name
        self.age = age
        self.height = height
        self.sal = sal
        self.man_id = man_id
        Employee.emp_count += 1


def main():
    file = './empManager_csv.csv'

    with open(file) as f:
        next(f)
        for line in f:
            emp_id, emp_name, age, height, sal, man_id = line.strip().split(',')
            e1 = Employee(emp_id,emp_name,age,height,sal,man_id)
        print(Employee.emp_count)


if __name__ == '__main__':
    main()



