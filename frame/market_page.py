#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:market_page.py
@time:2020/11/08
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy

from frame.base_page import BasePage
from frame.search_page import Search


class Market(BasePage):

    def goto_search(self):
        self.parse_yaml('./market_page.yml','goto_search')
        return Search(self.driver)



