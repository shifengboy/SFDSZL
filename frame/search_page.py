#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:search_page.py
@time:2020/11/08
"""
from appium.webdriver.common.mobileby import MobileBy

from frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys('alibaba')
        self.parse_yaml('search_page.yml','search')


