#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_workweixin.py
@time:2020/10/29
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWokrWeiXin:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "automationName": "UiAutomator2",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # caps["settings[waitForIdleTimeout]"] = 0
            "noReset": True,  # 不重置APP
            "skipServerInstallation": True,  # 跳过 uiAutomator2服务器安装
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,  # 跳过设备初始化
            "unicodeKeyboard": True,  # 默认启用 Unicode 输入
            "resetKeyboard": True  # 与上面合用，可以输入中文
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_workweixin_daka(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("工作台")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().text("打卡").'
                                                               'instance(0));').click()
        # settings
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("外出打卡")').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        assert WebDriverWait(self.driver, 10).until(lambda x: '打卡成功' in x.page_source)
