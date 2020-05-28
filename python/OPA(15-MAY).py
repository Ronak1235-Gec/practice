class Professor:
    def __init__(self,pid,pname,subjectDict):
        self.pid=pid
        self.pname=pname
        self.subjectDict=subjectDict
        
class University:
    def getTotalExperience(self,prof,reqid):
        total=0
        for i in prof:
            if i.pid==reqid:
                for j in i.subjectDict.values():
                    total=total+j 
        return total
    def selectSeniorProfessorBySubject(self,prof,reqsub):
        hexp=0
        hprof=None
        for i in prof:
            for subj,exp in i.subjectDict.items():
                if subj.lower()==reqsub.lower():
                    if exp>hexp:
                        hexp=exp
                        hprof=i 
        return hprof

if __name__=='__main__':
    univ=University()
    prof=[]
    c=int(input())
    for i in range(c):
        subjectDict={}
        pid=int(input())
        pname=input()
        sub=int(input())
        subjectDict={}
        for j in range(sub):
            subject=input()
            years=int(input())
            subjectDict[subject]=years
        P=Professor(pid,pname,subjectDict)
        prof.append(P)
    reqid=int(input())
    reqsub=input()
    print(univ.getTotalExperience(prof,reqid))
    professor=univ.selectSeniorProfessorBySubject(prof,reqsub)
    if professor==None:
        print("No Professor")
    else:
        print(professor.pid,professor.pname,professor.subjectDict)