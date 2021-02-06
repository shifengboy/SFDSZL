#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_TouchAction.py
@time:2020/10/17
"""

import time

from selenium import webdriver
from selenium.webdriver import TouchActions



class TestTouchAction():

    def setup_method(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
        pass
    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')
        el.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el_search)  # 点击
        action.perform()
        action.scroll_from_element(el, 0, 10000).perform()
        time.sleep(3)





