#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_select.py
@time:2020/11/13
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

class TestSelect:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
        pass

    def test_select(self):
        self.driver.get('http://sahitest.com/demo/selectTest.htm')
        s1 = self.driver.find_element_by_id('s1Id')
        Select(s1).select_by_index(1)
        s2 = self.driver.find_element_by_id('s2Id')
        Select(s2).select_by_value('o2')
        sleep(3)

    def test_table(self):
        self.driver.get('http://sahitest.com/demo/tableTest.htm')
        self.driver.find_element_by_xpath('//table[4]/tbody/tr[1]/td[2]/textarea').send_keys('aaaa')
        sleep(5)