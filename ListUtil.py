import Course
import StrUtil
import json
Bweek = dict()
AllCourse = [[[0]*12]*7]*20
def CourseToBweek(self):
    Bweek.update(self)

def getAllCourse():
    return AllCourse

#def getCourse(Bweek,Sweek):
def getCourse(i,j,k):
    #for i in range(int(Bweek)):
        #for j in range(int(Sweek)):
         #   for k in range(11):
  #              try:
                    if (AllCourse[int(i)][int(j)][int(k)] is not  None):
                        print ("读取的数据：" ,i,j,k)
                        print(AllCourse[int(i)][int(j)][int(k)])
                        # c = json.loads(StrUtil.dict2object(AllCourse[int(i)][int(j)][int(k)]))
                        c = StrUtil.dict2object(AllCourse[int(i)][int(j)][int(k)])

                        return c
#                except:
 #                   print (i,j,k, "error")

def addCourse(Course):

    for i in Course.gerForBWeek():
        #for j in Course.getForSWeek():
        for k in Course.getForSection():
            print("录入数据:", int(i), int(Course.getForSWeek()), int(k))
            # AllCourse[int(i)][int(Course.getForSWeek())][int(k)] = json.dumps(StrUtil.object2dict(Course))
            AllCourse[int(i)][int(Course.getForSWeek())][int(k)] = StrUtil.object2dict(Course)
            print("数据录入: ", AllCourse[int(i)][int(Course.getForSWeek())][int(k)])





