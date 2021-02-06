#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2020/11/08
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy

from frame.base_page import BasePage
from frame.market_page import Market


class Main(BasePage):
    def goto_market(self):
        # 制造假弹窗
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]').click()
        # self.find(MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        self.parse_yaml('./main_page.yml','goto_market')

        return Market(self.driver)
