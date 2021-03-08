#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_ios.py
@time:2021/02/24
"""
from appium import webdriver


class TestIos:
    def setup(self):
        desired_caps = {
            "platformName": "ios",
            "app": "/Users/chenshifeng/Library/Developer/Xcode/DerivedData/UICatalog-dchxrdgxvhwhyfghtfgzmhieqeqx/Build/Products/Debug-iphoneos/UICatalog.app",
            "automationName": "XCUITest",
            "deviceName": "SFdeiPad",
            "udid": "auto",
            "xcodeOrgId": "UYJV48339N",
            "xcodeSigningId": "Apple Development"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_ios(self):
        pass

    def teardown(self):
        self.driver.quit()

'''
xcodebuild -project /usr/local/lib/node_modules/appium/node_modules/_appium-webdriveragent@2.31.0@appium-webdriveragent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=00008101-000E449111E0001E' test

'''
