#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
host="https://idev.bhsgd.net/"
# host="https://insurance.chinavanda.com/"
class Regist():
    def __init__(self,s):
        self.session=s
    def regist_post(self,username,psw1,psw2,introduce):
        url=host+"jgx/client/holduser/regist"
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
    def is_regist_sucess(self,Expect ,Actual):
        if Expect in Actual:
            return True
        else:
            return False

if __name__ == "__main__":
    from page_obj.login_api import *
    s = requests.session()
    regist=Regist(s)
    r=regist.regist_post("其味无穷1","qwerqwerqwer123456","qwerqwerqwer123456","168496714invitation1520907287")
    print(r.content)
    data = r.json()
    print(data["cnmsg"])
    print(data["data"]["data"])
    # login=Login(s)
    # l=login.login_post("test003","123456")
    # print(l.content)
    # data2 = l.json()
    # print(data["cnmsg"])