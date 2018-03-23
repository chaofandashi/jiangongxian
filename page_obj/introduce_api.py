#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import *
import requests
host="https://idev.bhsgd.net/"
# host="https://insurance.chinavanda.com/"
class Introduce():
    def __init__(self,s):
        self.session=s

    def introduce_post(self):
        url=host+"jgx/client/seller/introduce/get"
        h={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
        }
        r=self.session.post(url,headers=h)
        return r

if __name__ == "__main__":
    from page_obj.login_api import *
    s=requests.session()
    # 登陆
    login=Login(s)
    l=login.login_post("168496714","bhs@mangohm")
    print(l.content)
    data2 = l.json()
    print(data2["cnmsg"])
    # 拿二维码
    introduce=Introduce(s)
    r=introduce.introduce_post()
    data=r.json()
    print(data["data"]["introduceCode"])

