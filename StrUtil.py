import re
def loadSweek(time): #时间:周五第3,4节{第7-12周}
    return {
        '周一' : 1,
        '周二' : 2,
        '周三' : 3,
        '周四' : 4,
        '周五' : 5,
        '周六' : 6,
        '周日' : 7,
    }.get(time[:2],'null')

def loadSection(time):
    return time[3:6]

def loadBweek(time): #正则
    regex = re.compile('{第[0-9]周}')
    pattern = re.findall(regex)
    res = re.findall(pattern,time)
    return res