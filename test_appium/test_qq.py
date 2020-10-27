#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_qq.py
@time:2020/10/27
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestQQ:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "automationName": "Appium",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.mobileqq",
            "appActivity": ".activity.SplashActivity",
            "noReset": "true",
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_unlock(self):
        TouchAction(self.driver).press(x=332,y=862).wait(200).move_to(x=584,y=862).wait(200).move_to(x=835,y=862).\
            wait(200).move_to(x=584,y=1112).wait(200).move_to(x=332,y=1368).wait(200).move_to(x=584,y=1368).\
            wait(200).move_to(x=835,y=1368).release().perform()
