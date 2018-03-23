#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
import time,datetime
import base64
host="https://idev.bhsgd.net/"
# host="https://insurance.chinavanda.com/"
class Order():
    def __init__(self,s):
        self.session = s
    # 填写表单内容
    def order_post(self,project_name,project_location,month):
        time_start = time.time()  # 获取时间戳
        # 获取month个月后的时间
        unix = datetime.datetime.now().replace(month=int(datetime.datetime.now().strftime('%m')) + month)
        time_end = int(time.mktime(unix.timetuple()))  # 转化为时间戳
        url=host+"jgx/client/order/begin"
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
                 "origin_insured": time_start,
                 "cycle_insured": 3,
                 "deadline_insured":time_end,
                 "construction_name": project_name,
                 "construction_local": project_location,
                 "billing_way": 1,
                 "billing_base": 200000,
                 "billing_percent": 2000000,
                 "billing_price": 30000000,
                 "dead_cost": "2000",
                 "hury_cost": "3000",
                 "hostipal_cost": "4000",
                 "phone": "",
                 "agreement": 1,
                 "productId": 1
                 }
        }
        r=self.session.post(url,json=body,headers=h)
        data = r.json()
        # 获取订单编号
        order_id = str(data["data"]["orderId"])
        return order_id
    # 获取七牛key和token
    def order_key_token(self,order_id):
        url = host+"jgx/client/order/examine/"+order_id
        h = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
        }
        r = self.session.post(url,headers=h)
        data = r.json()
        key = data["data"]["key"]
        token = data["data"]["token"]
        # key转base64
        base_key = base64.b64encode(key.encode('iso-8859-15'))
        # base64转utf-8
        str_key = base_key.decode('utf-8')
        return (str_key,token)
    # 上传图片
    def order_img(self, key, token, img_base64,img_url):
        # 上传图片地址
        url ="http://upload-z2.qiniup.com/putb64/-1/key/"+key
        h = {
            # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            # "Cookie":"sid=442gtsadk9smvaq3xwwdvtguh84dmtm3"
            'Content-Type': "application/x-www-form-urlencoded",
            "Authorization": "UpToken " + token,
            "Host": 'up-z2.qiniu.com',
        }
        body = img_base64
        r = self.session.post(url, data=body, headers=h)
        img_data = r.json()
        img_url.append(img_data["data"]["url"])
        return img_url
    # 提交订单
    def order_end(self,orderId,examine_pics):
        url = host+"jgx/client/order/verify"
        h = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
        }
        body = {
            "data": {
                "orderId": orderId,
                "examine_pics":examine_pics
            }
        }
        r = self.session.post(url, json=body, headers=h)
        return r.json()
if __name__ == "__main__":
    from page_obj.login_api import *
    s=requests.session()
    login = Login(s)
    login.login_post('god', 'bhs@mangohm')                        # 登录
    order=Order(s)                                                # 下单
    order_id=order.order_post("爱情公寓5","有米大楼",5)             # 保单填写 并获取订单id
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





    # 时间戳转为时间
    # print(datetime.datetime.fromtimestamp(t2))

