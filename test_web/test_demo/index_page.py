#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:index_page.py
@time:2020/10/25
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from test_web.test_demo.login_page import LoginPage
from test_web.test_demo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)
