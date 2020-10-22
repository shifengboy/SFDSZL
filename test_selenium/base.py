#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:base.py
@time:2020/10/17
"""
import os

from selenium import webdriver


class Base:
    def setup_class(self):
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('w3c', False)
        # self.driver = webdriver.Chrome(options=option)
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.phantomjs()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()
