#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_browser.py
@time:2020/10/31
"""
from time import sleep

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestBrowser:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "browserName": "Browser",
            # "appPackage": "com.tencent.mobileqq",
            # "appActivity": ".activity.SplashActivity",
            "deviceName": "5EN0219115000345",
            "noReset": "true",
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true",
            "chromedriverExecutable": "/Users/chenshifeng/Library/SoftWare/ChromeDriver/chromedriver-2.20",
            # "avd": "Pixel_23_6"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('https://m.baidu.com')
        with open('tmp.html','w') as f:
            print(self.driver.page_source, file=f)



    def test_deviceapi(self):
        self.driver.make_gsm_call('18658127166',GsmCallActions.CALL)
        self.driver.send_sms('13186860209','hello appium')

        self.driver.set_network_connection(1)
        sleep(3)
        self.driver.get_screenshot_as_file('./photos/img.png')
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)
        self.driver.open_notifications()

