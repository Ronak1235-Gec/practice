class Employee:
    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_salary=emp_salary
    def increase_salary(self,percentage):
        self.emp_salary+=self.emp_salary*percentage*0.01
        
class Organisation:
    def __init__(self,org_name,emp_list):
        self.org_name=org_name
        self.emp_list=emp_list
    def calculate_increment(self,emp_role,percentage):
        emp_res = []
        for i in self.emp_list:
            if i.emp_role==emp_role:
                i.increase_salary(percentage)
                emp_res.append(i)
        return emp_res


if __name__=='__main__':
    emp_list=[]
    count = int(input())
    for i in range(count):
        emp_id = int(input())
        emp_name = input()
        emp_role = input()
        emp_salary = int(input())
        obj=emp_list.append(Employee(emp_id,emp_name,emp_role,emp_salary))
    o=Organisation("TCS",emp_list)
    inp_role=input()
    inp_percentage=int(input())
    result=o.calculate_increment(inp_role,inp_percentage)
    if len(result)!=0:
        for i in result:
            print(i.emp_name,'\t',i.emp_salary)
    else:
        print("No Employee found with the given role.")
        
        