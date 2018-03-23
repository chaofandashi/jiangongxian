#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
host="https://idev.bhsgd.net/"
# host="https://insurance.chinavanda.com/"
class Update():
    def __init__(self,s):
        self.session=s
    def updata_post(self,company=None,phone=None,email=None):
        url=host+"jgx/client/holduser/info/update"
        h = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
        }
        body={
             "data": {
                "company": company,
                "phone": phone,
                "email": email
            }
        }
        r=self.session.post(url,json=body,headers=h)
        return r
if __name__ == "__main__":
    from page_obj.login_api import *
    s=requests.session()
    login=Login(s)
    r=login.login_post("168496714","bhs@mangohm")
    print(r.content)  # 查看返回值
    data = r.json()  # json化方便字典提取
    print(str(data["data"]["phone"]))  # 字典提取登陆成功账号
    updata=Update(s)
    # 修改信息
    r2=updata.updata_post(company="保护神123",phone='',email="275769643@qq.com")
    data2 = r2.json()
    print(data2)
