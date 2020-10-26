#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:1.1.py
@time:2020/09/27
"""
from appium import webdriver

des = {
       'resetKeyboard': True,
       'platformVersion': '6.0.1',
       'noReset': True, # 不将app初始化
       'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
       # 'appActivity': '.BrowserActivity',
       'appPackage': 'com.tencent.qqlite',
       # 'appPackage': 'com.android.browser',
       'unicodeKeyboard': True,
       'deviceName': 'emulator-5554',
       'platformName': 'Android'}
# print(des)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)









