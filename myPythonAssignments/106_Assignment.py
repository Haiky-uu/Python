# read employee manager file to build employee-manager tree and find out nearest common manager
# for any two employees given by user.

class Emp:

    def __init__(self,emp_id,emp_name,emp_age,emp_height,emp_sal,man_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_height = emp_height
        self.emp_sal = emp_sal
        self.man_id = man_id

e1ls = []
e2ls = []


def tree(empDict,ep1,ep2):
    #print(empDict)

    #print(ep1.man_id, ep2.man_id)
    e1ls.append(ep1.man_id)
    e2ls.append(ep2.man_id)

    if ep1.man_id == -1000 or ep2.man_id == -1000:
        print("end")
        return
    ep1 = empDict[ep1.man_id]
    ep2 = empDict[ep2.man_id]
    tree(empDict,ep1,ep2)


def main():
    pass
    empD= {}
    with open('./empManager_csv.csv','r') as f:
        next(f)
        for line in f:
            emp_id,emp_name,emp_age,emp_height,emp_sal,man_id = line.strip().split(',')
            e1 = Emp(int(emp_id),emp_name,int(emp_age),float(emp_height),int(emp_sal),int(man_id))
            empD[int(emp_id)] = e1

        ep1 = 11
        ep2 = 10
        ep1Obj = empD[ep1]
        ep2Obj = empD[ep2]
        tree(empD,ep1Obj,ep2Obj)

        print(e1ls,e2ls)
        for el in e1ls:
           if el in e2ls:
                print(f"Same Manager of {ep1Obj.emp_name} and {ep2Obj.emp_name} is {empD[el].emp_name}")
                break


if __name__ == '__main__':
    main()


