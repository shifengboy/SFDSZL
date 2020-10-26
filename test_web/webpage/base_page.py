#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:base_page.py
@time:2020/10/25
"""
# 基类 ：最基本的方法， driver 实例化， find()等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # driver: WebDriver
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            # 进行页面跳转的操作
            self.driver = driver
            self.driver.implicitly_wait(5)

        # base_url 打开某个页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element

    def wait_for_next(self, by1, locator1, by2, locator2):
        try:
            self.find(by1, locator1).click()
            return self.find(by2, locator2)
        except:
            return False

    # WebDriverWait(self.driver, 10).until(wait_for_next)
