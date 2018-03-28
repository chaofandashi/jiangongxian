#-*-coding:utf-8-*- 
from selenium import webdriver
#-*-coding:utf-8-*-
from selenium import webdriver
import request
import time,datetime
import base64
from page_obj.host_api import *
import re
class Continue_order():
    def __init__(self,s):
        self.session = s
    def get_url(self,status=0,postion=0):
        url=host+"/jgx/client/order/all"
        h={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
        }
        body={
            "data":{
                 "status": status,
                 "order": 1,
                 }
        }
        r=self.session.post(url,headers=h,json=body)
        date = r.json()
        api=date["data"]["data"][0]["buttons"][postion]["url"]
        api_split=api.split("?")[0]
        order_id=str(re.findall('\\d{1,10}$',api_split)[0])
        return order_id
    def continue_post(self,url):
        h={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
        }
        r = self.session.post(url, headers=h)
        return r
if __name__ == "__main__":
    from page_obj.login_api import *
    from page_obj.order_api import *
    s = requests.session()
    login = Login(s)
    login.login_post("god","bhs@mangohm")
    continue_order=Continue_order(s)
    # 输入订单状态100为全部，0-6分为待提交（0,1）、审核中、待修改（2,0）、待支付（3,2）、待核账、待出单、已出单
    orderId=continue_order.get_url(0,1)
    url=host+"/jgx/client/order/query/"+orderId
    res=continue_order.continue_post(url)
    print(orderId)
    data=res.json()
    order = Order(s)
    order_id = order.order_post(data["data"]["construction_name"],data["data"]["construction_local"],3,data["data"]["productId"],orderId)
    print(order_id)
    with open("../test_data/order_img/123.png", "rb") as f:                              # 图片转base64
        img_base64 = base64.b64encode(f.read())
    with open("../test_data/order_img/1234.png", "rb") as f:                             # 图片转base64
        img_base64_2 = base64.b64encode(f.read())
    token_key=order.order_key_token(order_id)                     # 获取七牛的token和key
    key1=token_key[0]
    token1=token_key[1]
    token_key = order.order_key_token(order_id)                   # 获取七牛的token和key
    key2=token_key[0]
    token2=token_key[1]
    img_url = []                                                  # 存图片url
    order.order_img(key1, token1, img_base64,img_url)               # 上传图片
    order.order_img(key2, token2, img_base64_2,img_url)             # 上传图片
    print(img_url)
    res=order.order_end(order_id, img_url)                        # 保单完成
    print(res["data"]["orderId"])                                 #获取订单号



    # project_name, project_location, month, productId = 1

