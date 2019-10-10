#CourseDict = {} #CourseDich = dict()  dict(key = 'cold')
#CourseDict = ''  {'key:' 'a'}
CourseList = []


class Course:
    cname = ''
    time = ''
    tname = ''
    pname = ''
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
