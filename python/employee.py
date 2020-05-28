class Employee:
    def __init__(self,ename,eid,age,gender,):
        self.ename=ename
        self.eid=eid
        self.age=age
        self.gender=gender
        
class Organization:
    def __init__(self,orgname,emps):
        self.orgname=orgname
        self.emps=emps
        
    def addEmployee(self,ename,eid,age,grnder):
        self.emps.append(Employee(ename,eid,age,gender))
        
    def getEmployeeCount(self):
        return len(self.emps)
        
    def findEmployeeAge(self,reqid):
        op=0
        for i in self.emps:
            if i.eid==reqid:
                op=i.age
        return op
        
    def countEmployees(self,reqage):
        count=0
        for i in self.emps:
            if i.age>reqage:
                count+=1
        return count
        

if __name__ == '__main__':
    emps=[]
    o=Organization('XYZ',emps)
    c=int(input())
    for i in range(c):
        ename=input()
        eid=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(ename,eid,age,gender)
    
    reqid=int(input())
    reqage=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(reqid))
    print(o.countEmployees(reqage))