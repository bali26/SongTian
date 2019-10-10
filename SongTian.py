import os
import re
import urllib.parse

import requests
from PIL import Image
from bs4 import BeautifulSoup
from lxml import etree
from Course import Course
import StrUtil
user = 0
url = "http://192.168.170.253/Default2.aspx"
S = requests.session()
header_code = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Referer": "http://192.168.170.253/",
    "Host": "192.168.170.253",
    "Cache-Control": "max-age=0"
}


def get_post_data(url):
    re = S.get(url).text
    soup = BeautifulSoup(re, 'lxml')
    # user = input("学号: ")
    # pwd = input("密码: ")
    global user
    user = 1908010101
    pwd = "bali1626"
    URL_CODE = "http://192.168.170.253/CheckCode.aspx"  # 验证码地址
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
for i in range(0,1):
    #print(str(res[i]))
    w = str(res[i]).split("<br>")
    cname = w[0]
    time = w[1]
    tname = w[2]
    pname = w[3]

    print("课名:" + cname)
    print("时间:" + time)
    print("老师:" + tname)
    print("地点:" + pname)
    c = Course(cname,time,tname,pname)



    StrUtil.loadBweek(c.getTime())
