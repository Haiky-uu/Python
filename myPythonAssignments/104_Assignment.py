# 104 read employee manager file (create class and functions OOP) and store in tree
# (you can built tree using dictionary)

class Employee:

    def __init__(self,emp_id,name,age,height,sal,manager_id):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.height = height
        self.sal = sal
        self.manager_id = manager_id
        #print(__name__)

    def tree(self,curr_emp, empdata):
        #print(empdata)
        if curr_emp.emp_id == 2:
            print(curr_emp.name,'\n',end="")
            #print("Root",end=" ")
        empid = curr_emp.emp_id
        for v in empdata.values():
            if v.manager_id == empid:
                print("---->",v.name,"\n",end="")
                curr_emp = empdata[v.emp_id]
                self.tree(curr_emp, empdata)
        #print("")


def main():
    print('Program')
    empData = {}
    file = './empManager_csv.csv'
    with open(file) as f:
        next(f)
        for line in f:
            emp_id,name,age,height,sal,manager_id = line.strip().split(',')
            e1 = Employee(int(emp_id),name,int(age),float(height),float(sal),int(manager_id))
            empData[int(emp_id)] = e1

    curr_emp = 2
    cur_obj = empData[curr_emp]
    e1.tree(cur_obj,empData)


if __name__ == '__main__':
    main()

