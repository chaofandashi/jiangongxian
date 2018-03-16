#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import *
from page_obj.order_api import *
import requests
import unittest
import urllib3
urllib3.disable_warnings()
class Order(unittest.TestCase):
    '''发帖测试'''
    def setUp(self):
        self.s = requests.session()
    def test_order1_normal(self):
        '''正确下单'''
        login = Login(self.s)
        login.login_post('168496714', 'bhs@mangohm')
        order = Order(self.s)
        order_id = order.order_post("是时候真正表演真正的技术了","大学城北",5)          # 填写表单信息
        with open("../test_data/order_img/1.png", "rb") as f:                    # 图片转base64
            img_base64_1 = base64.b64encode(f.read())
        with open("../test_data/order_img/12.png", "rb") as f:                   # 图片转base64
            img_base64_2 = base64.b64encode(f.read())
        key_token = order.order_key_token(order_id)                                # 获取七牛key与token
        key1 = key_token[0]
        token1 = key_token[1]
        key_token = order.order_key_token(order_id)
        key2 = key_token[0]
        token2 = key_token[1]
        img_url=[]                                                                 # 存图片url
        order.order_img(key1, token1, img_base64_1, img_url)                       # 上传图片
        order.order_img(key2, token2, img_base64_2, img_url)                       # 上传图片
        order.order_end(order_id,img_url)                                          # 下单成功进入审核