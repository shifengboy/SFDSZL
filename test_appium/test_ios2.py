#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_ios.py
@time:2021/02/24
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestIos:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        # desired_caps['platformVersion'] = '13.6'
        desired_caps['platformVersion'] = '14.2'
        # desired_caps['deviceName'] = 'SFdeiPad'
        desired_caps['deviceName'] = 'SFdeiPhone'
        desired_caps['bundleId'] = 'com.chenshifeng.apple-samplecode.UICatalog'
        desired_caps['udid'] = 'auto'
        desired_caps['xcodeOrgId'] = 'UYJV48339N'
        desired_caps['xcodeSigningId'] = 'iPhone Developer'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_ios(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Action Sheets').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Other').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Safe Choice').click()

    def teardown(self):
        self.driver.quit()

