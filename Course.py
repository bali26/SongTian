#CourseDict = {} #CourseDich = dict()  dict(key = 'cold')
#CourseDict = ''  {'key:' 'a'}
import StrUtil

CourseList = []


class Course:
    cname = ''
    time = ''
    tname = ''
    pname = ''
    def getIntTime(self,Sweek): #return list
        j = []
        for i in self.gerForBWeek():
            for k in self.getForSection():

                j.append((str(i)+str(Sweek)+str(k)))
        print("INT数据：" + str(j))
    def getCname(self):
        return self.cname
    def getTime(self):
        return self.time
    def getTname(self):
        return self.tname
    def getPname(self):
        return self.pname

    def setCname(self,cname):
        self.cname = cname
    def setTime(self,time):
        self.cname = time
    def setTname(self,tname):
        self.tname = tname
    def setPname(self,pname):
        self.cname = pname
    def gerForBWeek(self):
        return StrUtil.getForBweek(self.getTime())
    def getForSWeek(self):
        return StrUtil.loadSweek(self.getTime())
    def getForSection(self):
        return StrUtil.loadSection(self.getTime())
    def __init__(self,cname,time,tname,pname):
        self.cname = cname
        self.time = time
        self.tname = tname
        self.pname = pname
        CourseList.append(self)



def getCourseLists():
   return CourseList

def getCourse(name):
    for i in CourseList:

        if(CourseList[i] == name):
            return CourseList[i]