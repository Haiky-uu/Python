class Teacher:
    # int id;
    # string name;
    # float height;
    # float weight;
    # int age;
    #this class has id, name,height, weight, age
    # Student(id,name,height,weight,age)
    
    # Constructor of the class
    def __init__(self,id,name,edu,salary,height,weight,age):
        self.id = id
        self.name = name
        self.edu = edu
        self.salary = salary
        self.height = height
        self.weight = weight
        self.age = age
    
    def print_teacher(self):
        print("*****INSIDE Teacher CLASS PRINT METHOD*****")
        print("DETAILS FOR Teacher: ",self.id)
        print("NAME OF THE Teacher: ",self.name)
        print("EDU: ", self.edu)
        print("salary ",self.salary)
        print("HEIGHT: ",self.height)
        print("WEIGHT: ",self.weight)
        print("AGE: ",self.age)
        print("******************* Teacher DETAILS END *********************")
    
    ######## 
   ### def print_student_confidential(self):
     ###   print("pawwsord")
 