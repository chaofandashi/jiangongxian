#-*-coding:utf-8-*- 
from selenium import webdriver
D
from page_obj.host_api import *
class Product():
    def __init__(self,s):
        self.session = s
    def product_post(self):
        url=host+"/jgx/client/product/all"
        h = {
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
    login = Login(s)
    r = login.login_post('168496714', 'bhs@mangohm')
    print(r.content)             # 查看返回值
    data = r.json()              # json化方便字典提取
    res = str(data["data"]["username"])     # 字典提取登陆成功账号
    print(res)

    product=Product(s)
    r=product.product_post()
    data=r.json()
    print(data["data"][0])

