#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_actionchains.py
@time:2020/09/27
"""
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestDefaultSuite():
    def setup_method(self, ):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_key(self):
        self.driver.get('https://www.baidu.com/')
        dom = self.driver.find_element_by_id('kw')

        ActionChains(self.driver).key_down(Keys.SHIFT, dom).send_keys('a').send_keys('c').key_up(Keys.SHIFT).pause(2).perform()





