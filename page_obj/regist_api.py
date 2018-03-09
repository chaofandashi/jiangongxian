#-*-coding:utf-8-*- 
from selenium import webdriver
import requests

class Regist():
    def __init__(self,s):
        self.session=s
    def regist_post(self,username,psw1,psw2,introduce):
        url="https://idev.bhsgd.net/jgx/client/holduser/regist"
        h={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
        }
        body={
             "data": {
                "username": username,
                "password": psw1,
                 "confirmPassword":psw2,
                "introduceCode": introduce
            }
        }
        r=self.session.post(url,json=body,headers=h)
        return r

if __name__ == "__main__":
    from page_obj.login_api import *
    s = requests.session()
    regist=Regist(s)
    r=regist.regist_post("test003","123456","123456","168496714invitation1520593555")
    print(r.content)
    data = r.json()
    print(data["data"]["data"])
    login=Login(s)
    l=login.login_post("test003","123456")
    print(l.content)
    data2 = l.json()
    print(data["cnmsg"])