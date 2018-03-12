#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
from page_obj.regist_api import *
from page_obj.login_api import *
from page_obj.introduce_api import *
import unittest
class Test_regist(unittest.TestCase):
    u'''注册'''
    def setUp(self):
        self.s = requests.session()
    def tearDown(self):
        1
    def test_regist1_normal(self):
        u'''内推码正确登录'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('168496714', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()
        data=r.json()
        introduce_code=data["data"]["introduceCode"]
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("test10012","123456","123456",introduce_code)
        data2=res.json()
        print(regist.is_regist_sucess("成功",data2["cnmsg"]))
    def test_regist2_error(self):
        u'''已存在账号注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('168496714', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("test10012","123456","123456",introduce_code)#注册
        data2=res.json()                                                    # json化方便字典提取
        print(regist.is_regist_sucess("该用户名已注册",data2["cnmsg"]))       #断言
    def test_regist3_error(self):
        u'''失效内推码注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('168496714', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("test10015","123456","123456",introduce_code) # 注册1使用内推码
        res2=regist.regist_post("test10016","123456","123456",introduce_code)# 注册2再次使用内推码
        data2=res2.json()                                                    # json化方便字典提取
        print(regist.is_regist_sucess("无效的邀请码",data2["cnmsg"]))          #断言



