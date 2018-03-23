#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
from page_obj.regist_api import *
from page_obj.login_api import *
from page_obj.introduce_api import *
import unittest,random,time

class Test_regist(unittest.TestCase):
    u'''注册测试'''
    def setUp(self):
        self.s = requests.session()
        self.username = int(random.randint(1,10000000000))  # 获取随机数
    def tearDown(self):
        self.s.cookies.clear_session_cookies()
    def test_regist1_normal(self):
        u'''内推码正确注册'''
        #登录管理员账号
        login = Login(self.s)
        # 168496714
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()
        data=r.json()
        introduce_code=data["data"]["introduceCode"]
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post(self.username,"123456","123456",introduce_code)
        data2=res.json()
        print(regist.is_regist_sucess("成功",data2["cnmsg"]))
    def test_regist2_error(self):
        u'''已存在账号注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("test10017","123456","123456",introduce_code)#注册
        data2=res.json()                                                    # json化方便字典提取
        print(regist.is_regist_sucess("该用户名已注册",data2["cnmsg"]))       #断言
    def test_regist3_error(self):
        u'''已用过推码注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post(self.username,"123456","123456",introduce_code) # 注册1使用内推码
        res2=regist.regist_post("huang20180319","123456","123456",introduce_code)# 注册2再次使用内推码
        data2=res2.json()                                                    # json化方便字典提取
        print(regist.is_regist_sucess("无效的邀请码",data2["cnmsg"]))          #断言
    def test_regist4_error(self):
        u'''错误内推码注册'''
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post(self.username,"123456","123456","sdaffeasadf21")   # 注册1使用内推码
        res2=regist.regist_post(self.username,"123456","123456","123456wew789")   # 注册2再次使用内推码
        data1 = res.json()                                                      # json化方便字典提取
        data2=res2.json()
        print(regist.is_regist_sucess("无效的邀请码", data1["cnmsg"]))            # 断言
        print(regist.is_regist_sucess("无效的邀请码",data2["cnmsg"]))             # 断言
    def test_regist5_error(self):
        u'''账号为空注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("","123456","123456",introduce_code)         #注册1使用内推码
        data2=res.json()                                                    #json化方便字典提取
        print(regist.is_regist_sucess("用户名必须为字符串，长度为1~16，不得含有\\ & < >且不可缺省",data2["cnmsg"]))         #断言
    def test_regist6_error(self):
        u'''密码为空注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("qwer1234","","",introduce_code)         #注册1使用内推码
        data2=res.json()                                                    #json化方便字典提取
        print(regist.is_regist_sucess("密码必须为字符串，长度为6~16，不得含有\ & < >且不可缺省",data2["cnmsg"]))
    def test_regist7_error(self):
        u'''密码长度小于5或者大于16注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("qwer12345","qwerqwerqwer123456","qwerqwerqwer123456",introduce_code)#注册1使用内推码
        res2 = regist.regist_post("qwer12345", "qwer", "qwer", introduce_code)  # 注册1使用内推码
        data2 = res.json()
        data3=res.json()                                                        #json化方便字典提取
        print(regist.is_regist_sucess("密码必须为字符串，长度为6~16，不得含有\ & < >且不可缺省",data2["cnmsg"]))
        print(regist.is_regist_sucess("密码必须为字符串，长度为6~16，不得含有\ & < >且不可缺省", data3["cnmsg"]))
    def test_regist8_error(self):
        u'''账号长度小于5或者大于16注册'''
        #登录管理员账号
        login = Login(self.s)
        login.login_post('god', 'bhs@mangohm')
        # 获取内推码
        introduce=Introduce(self.s)
        r=introduce.introduce_post()                                        #获取内推码
        data=r.json()                                                       #json化方便字典提取
        introduce_code=data["data"]["introduceCode"]                        #赋值内推码
        # 注册
        regist=Regist(self.s)
        res=regist.regist_post("qwerqwerqwer123456","123456","qwerqwerqwer123456",introduce_code)#注册1使用内推码
        res2 = regist.regist_post("qwer1", "123456", "123456", introduce_code)  # 注册1使用内推码
        data2 = res.json()
        data3=res.json()                                                        #json化方便字典提取
        print(data3)
        print(regist.is_regist_sucess("用户名必须为字符串，长度为1~16，不得含有\\ & < >且不可缺省",data2["cnmsg"]))
        print(regist.is_regist_sucess("用户名必须为字符串，长度为1~16，不得含有\\ & < >且不可缺省", data3["cnmsg"]))