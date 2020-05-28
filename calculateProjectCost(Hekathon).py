#this is  only for practice purpose.
class Project:
    def __init__(self,projectId,projectName,manHours,technologyList):
        self.projectId=projectId
        self.projectName=projectName
        self.manHours=manHours
        self.technologyList=technologyList
        self.avgProjCost=0
        
    def calculateProjCost(self,rate):
        cost = self.manHours*rate;
        return cost
        
class Organization:
    def __init__(self,orgName,projectList):
        self.orgName=orgName
        self.projectList=projectList
        
    def projAvgCostByTechnology(self,projId,rate):
        # self.rate=rate
        # self.projectId=projectId
        for i in self.projectList:
            if(i.projectId==projId):
                i.avgProjCost = (Project.calculateProjCost(i,rate))/(len(i.technologyList))
                return i
if __name__=='__main__':
    projectList=[]
    
    N=int(input())
    for i in range(N):
        projectId=int(input())
        projectName=input()
        manHours=int(input())
        M=int(input())
        technologyList=[]
        for j in range(M):
            technologyList.append(input())
        P=Project(projectId,projectName,manHours,technologyList)
        projectList.append(P)            
    org=Organization("ABC",projectList)
    projId=int(input())
    rate=int(input())
    avgProj=org.projAvgCostByTechnology(projId,rate)        
    if avgProj==None:
        print("No Project Exists")  
    else:
        print(avgProj.projectId,avgProj.projectName,avgProj.manHours,avgProj.technologyList,
              avgProj.avgProjCost)    
        
            
            
                   



  
