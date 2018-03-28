#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import *
from page_obj.host_api import *
class Get_info():
    def __init__(self,s):
        self.session=s
    def info_post(self):
        url=host+"/jgx/client/holduser/info/get"
        h={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
        }
        r=self.session.post(url,headers=h)
        return r
    def is_success_updata(self,Expect,Actual):
        if Expect in Actual:
            return True
        else:
            return False
if __name__ == "__main__":
    s=requests.session()
    # 登陆
    login=Login(s)
    login.login_post("168496714","bhs@mangohm")
    info_get=Get_info(s)
    r=info_get.info_post()
    data=r.json()
    print(data)
    print(data["data"]["username"])
