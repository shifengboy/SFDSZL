#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:login_page.py
@time:2020/10/25
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from test_web.test_demo.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)