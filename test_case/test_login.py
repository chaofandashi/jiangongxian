#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import *
import requests
import unittest
import urllib3
urllib3.disable_warnings()
class Test_login(unittest.TestCase):
    u'''登陆测试'''
    def setUp(self):
        self.s = requests.session()
    def test_login1_normal(self):
        u'''正确账号密码登陆'''
        login = Login(self.s)
        r = login.login_post('168496714', 'bhs@mangohm')           #登陆
        data = r.json()                                           # json化方便字典提取
        res = str(data["data"]["username"])                       # 字典提取登陆成功账号进行断言
        print(login.is_login_sucess('168496714', res))            # 断言
    def test_login2_error(self):
        u'''正确账号错误密码登陆'''
        login=Login(self.s)
        r=login.login_post("qq996","11111")                        #登陆
        data = r.json()                                           # json化方便字典提取
        res = str(data["cnmsg"])                                  # 字典提取登陆失败信息进行断言
        print(login.is_login_fail(u"密码输入错误",u"密码错误",res))  # 断言
    def test_login3_error(self):
        u'''不存在账号密码登陆'''
        login=Login(self.s)
        r=login.login_post("16849671","bhs@mangohm")                        #登陆
        data = r.json()                                           # json化方便字典提取
        res = str(data["cnmsg"])                                  # 字典提取登陆失败信息进行断言
        print(login.is_login_fail(u"用户不存在",u"用户不存在",res))  # 断言

    def tearDown(self):
        self.s.cookies.clear_session_cookies()                    # 每次用例之后，清空cookie

if __name__ == "__main__":
    unittest.main()