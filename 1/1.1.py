#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:1.1.py
@time:2020/09/27
"""

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "automationName": "Appium",
    "deviceName": "emulator-5554",
    "appPackage": "com.tencent.mobileqq",
    # "appActivity": ".view.WelcomeActivityAlias",
    "appActivity": ".activity.SplashActivity",
    "noReset": "true",
    "dontStopAppOnReset": "true",
    "skipDeviceInitialization": "true",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)







