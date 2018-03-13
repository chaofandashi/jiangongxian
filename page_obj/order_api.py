#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
import time,datetime

class Order():
    def __init__(self,s):
        self.session = s
    def order_post(self,project_name,project_location,start,end):
        url="https://idev.bhsgd.net/jgx/client/order/begin"
        h = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
        }
        body={
            "data":{
                 "name": "黄军平",
                 "coi": "44522419920316155X",
                 "origin_insured": start,
                 "cycle_insured": 3,
                 "deadline_insured":end,
                 "construction_name": project_name,
                 "construction_local": project_location,
                 "billing_way": 1,
                 "billing_base": 200000,
                 "billing_percent": 2000000,
                 "billing_price": 30000000,
                 "dead_cost": "2000",
                 "hury_cost": "3000",
                 "hostipal_cost": "4000",
                 "phone": "13076220975",
                 "agreement": 1,
                 "productId": 2
                 }
        }
        r=self.session.post(url,json=body,headers=h)
        return r

if __name__ == "__main__":
    # from page_obj.login_api import *
    # s=requests.session()
    # login = Login(s)
    # r = login.login_post('168496714', 'bhs@mangohm')
    # # 下单
    # start_unix = time.time()                             # 获取时间戳
    # #获取两个月后的时间
    # unix=datetime.datetime.now().replace(month=int(datetime.datetime.now().strftime('%m'))+3)
    # end_unix=int(time.mktime(unix.timetuple()))          # 转化为时间戳
    # order=Order(s)
    # r=order.order_post("爱情公寓2","有米大楼",start_unix,end_unix)
    # data=r.json()
    # print(data)
    with open(r"C:\Users\27576\Desktop\449.jpg","rb") as f:
        print(f)

    # 时间戳转为时间
    # print(datetime.datetime.fromtimestamp(t2))

