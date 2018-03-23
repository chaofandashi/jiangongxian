#-*-coding:utf-8-*-
from selenium import webdriver
import unittest
from common import HTMLTestRunner
import os,time

base_path=os.path.realpath(os.path.dirname(__file__))
# 相对路径
case_path=os.path.join(base_path,"test_case")
report_path=os.path.join(base_path,"test_report")
discover=unittest.defaultTestLoader.discover(case_path,"test*.py")
# nowtime = time.strftime("%Y-%m-%d_%H_%M_%S")
htmlpath=os.path.join(report_path,"result.html")

with open(htmlpath,"wb") as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title="建工险测试用例报告",
                                           description="关于客户端注册、登录、下单的操作")
    runner.run(discover)