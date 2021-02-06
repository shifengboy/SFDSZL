#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_grid.py
@time:2020/12/26
"""
import time

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestGrid:
    def setup_method(self):
        self.driver = webdriver.Remote('http://127.0.0.1:5001/wd/hub')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_grid(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')
        el.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el_search)  # 点击
        action.perform()
        action.scroll_from_element(el, 0, 10000).perform()
        time.sleep(5)
