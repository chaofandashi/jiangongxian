#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
from page_obj.host_api import *

class Login():
    def __init__(self,s):
        self.session = s

    def login_post(self,username,psw):
        url = host+"/jgx/client/holduser/login"
        h = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
        }
        body = {
            "data": {
                "username": username,
                "password": psw,
                "isAutoLogin": True
            }
        }
        r = self.session.post(url, json=body, headers=h)
        return r
    # 成功断言
    def is_login_sucess(self,Expect ,Actual):
        if  Expect in Actual:
            return True
        else:
            return False
    # 失败断言
    def is_login_fail(self,Expect1,Expect2,Actual):
        if Expect1 in Actual or Expect2 in Actual:
            return True
        else:
            return False
if __name__ == "__main__":
    s = requests.session()
    login = Login(s)                    # 实例化
    r = login.login_post('god','bhs@mangohm')
    print(r.content)                    # 查看返回值
    data = r.json()                     # json化方便字典提取
    res = str(data["cnmsg"]) # 字典提取登陆成功账号
    print(login.is_login_sucess(res,'168496714'))      # 断言
    print(data["cnmsg"])