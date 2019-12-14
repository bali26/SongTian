import pickle
import re


def loadSweek(time):  # 时间:周五第3,4节{第7-12周}

    return {
        '周一': 1,
        '周二': 2,
        '周三': 3,
        '周四': 4,
        '周五': 5,
        '周六': 6,
        '周日': 7,
    }.get(time[:2], 'null')


def loadSection(time):
    regex = '[0-9]*'
    pattern = re.compile(regex)
    res = re.findall(pattern, str(time).split("{")[0])
    res = list(set(res))
    res.pop(0)
    print("RRES:", res)
    return res
    # list.append(time[3])
    # list.append(time[5])
    # print("time[6]:"+time[6])
    # print("time[5]:"+time[5])
    # print("time[4]:"+time[4])
    # return time[3:6]


def loadBweek(time):  # 正则 #5-19
    regex = '[0-9]*-[0-9]*'
    pattern = re.compile(regex)
    res = re.findall(pattern, time)
    return res


def getForBweek(s):
    ss = str(loadBweek(s)[0]).split("-")
    list = []
    #print("ss[0]:" + ss[0])
    #print("ss[1]:" + ss[1])
    if int(ss[0]) == int(ss[1]):
        #print("ss相等 返回" + ss[0])
        return range(int(ss[0]), int(ss[0]) + 1)
    else:
        for i in range(int(ss[0]), int(ss[1]) + 1):
            list.append(i)
            #print("打印大周:" + str(i));
        return list;


def object2dict(obj):
    return pickle.dumps(obj);


def dict2object(d):
    # new_obj = pickle.loads(d)
    # new_obj.dump()

    return pickle.loads(d)
#
# JSON transfer
# def object2dict(obj):
#     d = {}
#     d['__class__'] = obj.__class__.__name__
#     d['__module__'] = obj.__module__
#     d.update(obj.__dict__)
#     return d
#
#
# def dict2object(d):
#         print("D:" , d)
#    if '__class__' in d:
#         d = dict(eval(d))
#         class_name = d.pop('__class__')
#         module_name = d.pop('__module__')
#         module = __import__(module_name)
#         class_ = getattr(module, class_name)
#         for ii in d.items():
#             print(ii)
#         args = dict((key.encode('ascii'), value) for key, value in d.items())
#         inst = class_(**args)  # create new instance
#     else:
#         inst = d
#         return inst
