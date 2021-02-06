#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_webview.py
@time:2020/11/29
"""
from time import sleep

from appium import webdriver


class TestWebview:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "8.0",
            "automationName": "UiAutomator2",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.android.apis",
            "appActivity": "com.example.android.apis.ApiDemos",
            "chromedriverExecutable": "/Users/chenshifeng/Library/SoftWare/ChromeDriver/chromedriver74",
            # "appActivity": ".common.MainActivity",
            "noReset": True,  # 不重置APP
            # "autoGrantPermissions": True,
            # "skipServerInstallation": True,  # 跳过 uiAutomator2服务器安装
            # "dontStopAppOnReset": True,
            # "skipDeviceInitialization": True,  # 跳过设备初始化
            # "unicodeKeyboard": True,  # 默认启用 Unicode 输入
            # "resetKeyboard": True,  # 与上面合用，可以输入中文
            # "newCommandTimeout": 300
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_xpath('//*[contains(@text,"Views")]').click()
        print(self.driver.contexts)

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("WebView").'
                                                        'instance(0));').click()
        sleep(5)
        # with open('tmp.html','w') as f:
        #     print(self.driver.page_source, file=f)
        # self.driver.find_element_by_xpath('//*[contains(@text,"Hello World! - 1")]').click()
        print(self.driver.contexts)
        # self.driver._switch_to.context(self.driver.contexts[-1])
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element_by_xpath('/html/body/a').click()

        # print(self.driver.page_source)
        sleep(5)
