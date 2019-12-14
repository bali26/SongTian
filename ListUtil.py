from PyQt5.QtWidgets import QLabel, QGridLayout

import StrUtil
from prettytable import PrettyTable
Bweek = dict()

def printBweek():
    for key in Bweek.keys():
        print('key = {}'.format(key))
def printBweek2():
    list = sorted(Bweek.items(),key = lambda d:d[0]) #Bweek.items()
    table = PrettyTable(["上课时间","课程名字","老师名字","地点"])
    #table.field_names = ["上课时间","课程名字","老师名字","地点"]

    for tup in list:
        c = TimeToCourse(str(tup[0]))
        table.add_row([c.getTime(),c.getCname(),c.getTname(),c.getPname()])
    print(table)

def printBweek3(time): #根据大周遍历 Bweek + "-"
    list = dict()
    table = PrettyTable(["上课时间", "课程名字", "老师名字", "地点"])
    for elem in sorted(Bweek.items(), key=lambda d: (str(d[0]).split('-')[1],str(d[0]).split('-')[2])): #返回时间
        obj = TimeToCourse(elem[0])
        for bweek in obj.gerForBWeek():
            if ((str(bweek)).startswith(time)):  # 比较时间
                list.setdefault(obj.getTime(),obj)
    for elem2 in list.items():
        obj = list.get(elem2[0])
        table.add_row([obj.getTime(), obj.getCname(), obj.getTname(), obj.getPname()])
    print(table)





    # list = sorted(Bweek.items(),key = lambda d:d[0]) #Bweek.items()
    # table = PrettyTable(["上课时间","课程名字","老师名字","地点"])
    # #table.field_names = ["上课时间","课程名字","老师名字","地点"]
    #
    # for tup in list:
    #     c = TimeToCourse(str(tup[0]))
    #     table.add_row([c.getTime(),c.getCname(),c.getTname(),c.getPname()])

    #print(table)


def CourseToBweek(value, c):
    Bweek.setdefault(value, c)


def TimeToCourse(time):
    return StrUtil.dict2object(Bweek.get(time))


def getCourse(i, j, k):
    print("读取的数据：", i, j, k)
    c = TimeToCourse(str(i) +"-" + str(j) +"-" + str(k)) #14-2-3
    return c


def addCourse(Course):
    for i in Course.gerForBWeek():
        for k in Course.getForSection():
            print("录入的数据：", i, Course.getForSWeek(), k)
            CourseToBweek(str(i)+"-" + str(Course.getForSWeek()) +"-" + str(k), StrUtil.object2dict(Course))
#
# def printBweek3(time): #根据大周遍历 Bweek + "-"
#     list = []
#
#     for elem in Bweek.items(): #返回时间
#         print("elem:", elem[0])
#         obj = TimeToCourse(elem[0])
#         for bweek in obj.gerForBWeek():
#             if (str(bweek).startswith(time)):  # 比较时间
#                 print("OK!")
#                 list.append(elem)
#
#         print(list)
#     table = PrettyTable(["上课时间", "课程名字", "老师名字", "地点"])
#     for tup in list:
#         c = TimeToCourse(str(tup[0]))
#         table.add_row([c.getTime(), c.getCname(), c.getTname(), c.getPname()])
#     print(table)

def initLabel(time):
    list = dict()
    for elem in sorted(Bweek.items(), key=lambda d: (str(d[0]).split('-')[1], str(d[0]).split('-')[2])):  # 返回时间
        obj = TimeToCourse(elem[0])
        for bweek in obj.gerForBWeek():
            if ((str(bweek)).startswith(time)):  # 比较时间
                list.setdefault(obj.getTime(), obj)
                #每周需要的课程list
    grid = QGridLayout()
    for elem2 in list.items(): #elem2 ('周四第5,6节{第5-19周}', <Course.Course object at 0x0000020DC4C5DB70>)
        obj = list.get(elem2[0])# 周一 周二
        Label = QLabel();
        context = obj.getTime()+"\n" + obj.getCname()+"\n" + obj.getTname()+"\n" + obj.getPname()
        Label.setText(context)
        column = int(obj.getForSWeek()) #列 周数
        Sn = int(obj.getForSection()[0])
        grid.addWidget(Label, Sn,column)
    return grid


# def initLabel(time):
#     list = dict()
#     list2 = []
#     for elem in sorted(Bweek.items(), key=lambda d: (str(d[0]).split('-')[1], str(d[0]).split('-')[2])):  # 返回时间
#         obj = TimeToCourse(elem[0])
#         for bweek in obj.gerForBWeek():
#             if ((str(bweek)).startswith(time)):  # 比较时间
#                 list.setdefault(obj.getTime(), obj)
#     for elem2 in list.items():
#         obj = list.get(elem2[0])
#
#         grid = QGridLayout()
#
#         list2.append([obj.getTime(), obj.getCname(), obj.getTname(), obj.getPname()])
#     positions = [(i, j) for i in range(5) for j in range(5)]
#     for positions, list2 in zip(positions, list2):
#         Label = QLabel()
#         a = ""
#         for list22 in list2:
#             print("list022: ", list22)
#             if(str(list22).startswith('周')):
#
#             else:
#                 a = a + list22 + "\n"
#         print("list22: ", a)
#         Label.setText(a)
#
#         grid.addWidget(Label, *positions)
#
#     return grid