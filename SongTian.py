import sys
import os
import re
import urllib.parse
import requests
from PIL import Image
from bs4 import BeautifulSoup
from lxml import etree
import ListUtil
import StrUtil
#from PyQt5.QtWidgets import QApplication, QWidget
from Course import Course


user = 0
url = "http://192.168.170.253/Default2.aspx"
#url = "http://jwxt.sontan.net"
S = requests.session()
header_code = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Referer": "http://192.168.170.253/",
    #"Referer": "http://jwxt.sontan.net",
    "Host": "192.168.170.253",
    #"Host": "http://jwxt.sontan.net",
    "Cache-Control": "max-age=0"
}

def addcour(res):
    split_res = res.split('<br><br>')
    for i in range(0,len(split_res)):
        line = split_res[i]
        if(str(line).startswith('<font')):
            continue
        else:
            addc(line)
def addc(w):
    w = w.split("<br>")
    cname = w[0]
    time = w[1]
    tname = w[2]
    pname = w[3]
    print("2课名:" + cname)
    print("2时间:" + time)
    print("2老师:" + tname)
    print("2地点:" + pname)
    c = Course(cname, time, tname, pname)
    StrUtil.loadBweek(c.getTime())
    print(StrUtil.loadSweek(c.getTime()))
    print(StrUtil.loadSection(c.getTime()))
    ListUtil.addCourse(c)


def get_post_data(url):
    re = S.get(url).text
    soup = BeautifulSoup(re, 'lxml')
    # user = input("学号: ")
    # pwd = input("密码: ")
    global user
    user = 1908010101
    pwd = "bali1626"
    URL_CODE = "http://192.168.170.253/CheckCode.aspx"  # 验证码地址
    #URL_CODE = "http://jwxt.sontan.net/CheckCode.aspx"  # 验证码地址
    code = S.get(URL_CODE, headers=header_code)

    with open("code.gif", "wb") as f:
        f.write(code.content)
        print("保存验证码到" + os.getcwd() + "/code.gif" + "\n")

    image = Image.open('{}/code.gif'.format(os.getcwd()))
    image.show()
    checkCode = input("验证码: ")

    viewState = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    #	<form name="form1" method="post" action="Default2.aspx" id="form1">
    #   <input type="hidden" name="__VIEWSTATE" value="dDwyODE2NTM0OTg7Oz4=" />
    login_info = {
        # post data
        "__VIEWSTATE": viewState,
        # "__EVENTVALIDATION": '',
        "txtUserName": user,
        "TextBox2": pwd,
        "txtSecretCode": checkCode,
        "RadioButtonList1": "%D1%A7%C9%FA",  # "学生".encode('gb2312','replace')
        "Button1": "",
        "lbLanauage": "",
        "hidPdrs": "",
        "hidsc": "",
    }
    return login_info


response = S.post(url, data=get_post_data(url), headers=header_code)

def getInfor(response, xpath):
    content = response.content.decode('gb2312')  # 网页源码是gb2312要先解码
    selector = etree.HTML(content)  # __Elements对象
    infor = selector.xpath(xpath)[0]  # xpath 寻找指定label
    return infor  # string


text = getInfor(response, '//*[@id="xhxm"]/text()')
text = text.replace(" ", "")
studentname = text.replace("同学", "")
print("姓名：" + studentname)

if studentname is None:
    print("Login Failed")
else:
    print("Login successfully")
urlStudentname = urllib.parse.quote_plus(str(studentname.encode('gb2312')))

class_header = {
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #"Accept-Encoding": "gzip, deflate",
    #"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7",
    #"Host": "192.168.170.253",
    "Referer": "http://192.168.170.253/xskbcx.aspx?xh="+str(user)+"&xm="+urlStudentname+"&gnmkdm=N121603",
    #"Referer": "http://192.168.170.253/xskbcx.aspx?xh=1908010101&xm=%CB%D5%B3%AC%CF%CD&gnmkdm=N121603",
    #"Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

response = S.get("http://192.168.170.253/xskbcx.aspx?xh="+str(user)+"&xm="+urlStudentname+"&gnmkdm=N121603")
response = S.get("http://192.168.170.253/xskbcx.aspx?xh="+str(user)+"&xm="+urlStudentname+"&gnmkdm=N121603",headers=class_header)

html = response.content.decode("gb2312")
#print (html)

s = response.content.decode('gbk')
regex = '<td [\s\S]*?>([\s\S]*?)<\/td>'
pattern = re.compile(regex)
res= re.findall(pattern, s)


for i in range(0,18):
    res.remove(res[0])
res = list(set(res))
res.remove("&nbsp;")
res.remove("晚上")
res.remove("下午")
for i in range(0,len(res)):

    print("test2:" +(res[i]))
    #w = str(res[i]).split("<br>")
    addcour(res[i])
#ListUtil.printBweek2()




#ListUtil.printBweek3(Bweek)

#c.getIntTime(Sweek)



class Example(QWidget): #extend QWidget
    def __init__(self): #父类构造器
        super().__init__() #父级
        self.initUI()

    def initUI(self): #本类构造器

        Bweek = input("请输入大周:")
        Sweek = input("请输入小周:")
        Section = input("请输入节数:")
        c = ListUtil.getCourse(Bweek, Sweek, Section)

        print(c.getCname())
        print(c.getTname())
        print(c.getPname())
        print(c.getTime())
        grid = ListUtil.initLabel(Bweek)
        #grid = QGridLayout()
        self.setLayout(grid)
        self.move(300,150)
        self.setWindowTitle("松田课表")
        self.show()



app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())




