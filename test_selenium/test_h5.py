#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_h5.py
@time:2020/11/17
"""
from time import sleep

from selenium import webdriver


class TestH5:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    
    def test_h5(self):
        self.driver.get('https://www.baidu.com/')
        timing = self.driver.execute_script('return window.performance.timing')
        dns = timing['domainLookupEnd'] - timing['domainLookupStart']
        print(dns)
