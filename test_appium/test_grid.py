#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_grid.py
@time:2020/11/14
"""
import os
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": os.getenv('version'),
            "automationName": "UiAutomator1",
            "deviceName": "emulator-5554",
            "udid": os.getenv('udid'),
            "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "appActivity": ".common.MainActivity",
            "noReset": True,  # 不重置APP
            # "autoGrantPermissions": True,
            "skipServerInstallation": True,  # 跳过 uiAutomator2服务器安装
            # "dontStopAppOnReset":True,
            # "skipDeviceInitialization": True,  # 跳过设备初始化
            "unicodeKeyboard": True,  # 默认启用 Unicode 输入
            "resetKeyboard": True,  # 与上面合用，可以输入中文
            # "newCommandTimeout": 300
        }
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://192.168.56.1:4444/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
        pass

    @pytest.mark.parametrize('searchkey',[
        '阿里巴巴',
        '京东',
        '小米'
    ])
    def test_search(self, searchkey):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_xpath(f'//*[@resource-id="com.xueqiu.android:id/name" and @text="{searchkey}"]').click()
        self.driver.find_element_by_xpath('//*[@text="股票"]').click()
