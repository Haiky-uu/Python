
# build employee-manager tree using  and findout hierarchy for any given employee. For example if user gives "Pranav" as input,
# findout all managers of Pranav till top boss. Sample output: Pranav ==> Mandar ==> Soham ==> Ishan ==> Swati ==> Saurabh

class Employee:

    def __init__(self,e_id,name,age,ht,sal,m_id):
        self.e_id = e_id
        self.name = name
        self.age = age
        self.ht = ht
        self.sal = sal
        self.m_id = m_id


    def prog(self,emp_dict,new_emp,cnt):

        if new_emp.m_id == -1000:
            print(new_emp.name,end="")
            print("----> Root Node")
            print("node--->"*cnt[0],"Root Node")
            return
        print(new_emp.name,"----> ",end="")

        new_emp = emp_dict[new_emp.m_id]
        cnt[0]+=1
        self.prog(emp_dict,new_emp,cnt)
        print(cnt)




def main():
    emp_dict = {}
    with open('./empManager_csv.csv') as f:
        next(f)
        for line in f:
           e_id, name, age, ht, sal, m_id = line.strip().split(',')
           e1 = Employee(int(e_id),name,int(age),float(ht),int(sal),int(m_id))
           emp_dict[int(e_id)]=e1
    print(emp_dict)

    emp = 17
    new_emp = emp_dict[emp]
    cnt = [0]
    e1.prog(emp_dict,new_emp,cnt)


if __name__ == "__main__":
    main()


