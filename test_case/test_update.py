#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import *
from page_obj.update_api import *
import unittest
from page_obj.getinfo_api import *
class Test_updata(unittest.TestCase):
    '''修改个人信息'''
    def setUp(self):
        self.s = requests.session()
    def tearDown(self):
        self.s.cookies.clear_session_cookies()
    def test_updata1_normal(self):
        '''修改公司、联系电话、邮箱'''
        login=Login(self.s)
        r=login.login_post("god","bhs@mangohm")
        updata=Update(self.s)
        # 修改信息
        updata.updata_post(company="保护神科技有限公司",phone='13076220975',email="275769643@qq.com")
        info=Get_info(self.s)
        r=info.info_post()
        data=r.json()
        print(data)
        print(info.is_success_updata("保护神科技有限公司",data["data"]["company"]))
        print(info.is_success_updata("13076220975", data["data"]["phone"]))
        print(info.is_success_updata("275769643@qq.com", data["data"]["email"]))
    def test_updata2_normal(self):
        '''公司为空、联系电话不为空、邮箱不为空'''
        login=Login(self.s)
        r=login.login_post("god","bhs@mangohm")
        updata=Update(self.s)
        # 修改信息
        updata.updata_post(company="", phone='13076220975', email="275769643@qq.com")
    def test_updata3_normal(self):
        '''公司不为空、联系电话为空、邮箱不为空'''
        login=Login(self.s)
        r=login.login_post("god","bhs@mangohm")
        updata=Update(self.s)
        # 修改信息
        updata.updata_post(company="保护神科技有限公司",phone='',email="275769643@qq.com")
    def test_updata4_normal(self):
        '''公司不为空、联系电话不为空、邮箱为空'''
        login=Login(self.s)
        r=login.login_post("god","bhs@mangohm")
        updata=Update(self.s)
        # 修改信息
        updata.updata_post(company="保护神科技有限公司", phone='13076220975', email="")
    def test_updata5_normal(self):
        '''公司为空、联系电话为空、邮箱为空'''
        login = Login(self.s)
        r = login.login_post("god", "bhs@mangohm")
        updata = Update(self.s)
        # 修改信息
        updata.updata_post(company="", phone='', email="")
    def test_updata6_error(self):
        '''联系电话不足11位数以及超出11位和错误手机号'''
        login = Login(self.s)
        r = login.login_post("god", "bhs@mangohm")
        updata = Update(self.s)
        # 修改信息
        r=updata.updata_post(company="", phone='130762200', email="")
        r2 = updata.updata_post(company="", phone='130762209755', email="")
        r3 = updata.updata_post(company="", phone='12345678971', email="")
        data=r.json()
        data2 = r2.json()
        data3 = r3.json()
        info = Get_info(self.s)
        print(info.is_success_updata("请填写正确的手机号",data["cnmsg"]))
        print(info.is_success_updata("请填写正确的手机号", data2["cnmsg"]))
        print(info.is_success_updata("请填写正确的手机号", data3["cnmsg"]))
    def test_updata7_error(self):
        '''邮箱格式错误'''
        login = Login(self.s)
        r = login.login_post("god", "bhs@mangohm")
        updata = Update(self.s)
        # 修改信息
        r = updata.updata_post(company="", phone='', email="275769643@qq")
        r2 = updata.updata_post(company="", phone='', email="275769643.com")
        data = r.json()
        data2 = r2.json()
        info = Get_info(self.s)
        print(info.is_success_updata("电子邮箱必须为正确格式的邮箱", data["cnmsg"]))
        print(info.is_success_updata("电子邮箱必须为正确格式的邮箱", data2["cnmsg"]))
