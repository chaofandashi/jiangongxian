#-*-coding:utf-8-*- 
from selenium import webdriver
import request
from page_obj.host_api import *
import re
class Order_delete():
    def __init__(self,s):
        self.session = s
    def delete_draft(self,status=0,postion=0):
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
        print(date["data"]["data"][0]["buttons"][postion]["url"])
        try:
            api_url = date["data"]["data"][0]["buttons"][postion]["url"]
            url = api_url.split("://")[1]
            product_id = re.findall('\\d{1,10}$', date["data"]["data"][0]["buttons"][postion]["url"])
            # s.post(host + url)
            return product_id[0]
        except Exception as e:
            print("没有数据可删除")
if __name__ == "__main__":
    from page_obj.login_api import *
    s = requests.session()
    login = Login(s)
    login.login_post("god","bhs@mangohm")
    order=Order_delete(s)
    # 输入订单状态100为全部，0-6分为待提交（0,0）、审核中、待修改（2,1）、待支付（3,0）、待核账、待出单、已出单
    r=order.delete_draft(3,0)
    print("删除订单号为：%s"%r)
