#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_xueqiu.py
@time:2020/10/24
"""
import os
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "automationName": "UiAutomator2",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "appActivity": ".common.MainActivity",
            "noReset": True,  # 不重置APP
            # "autoGrantPermissions": True,
            "skipServerInstallation": True,  # 跳过 uiAutomator2服务器安装
            "dontStopAppOnReset":True,
            "skipDeviceInitialization": True,  # 跳过设备初始化
            "unicodeKeyboard": True,  # 默认启用 Unicode 输入
            "resetKeyboard": True,  # 与上面合用，可以输入中文
            # "newCommandTimeout": 300
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
        pass

    def test_search(self):
        '''
        1、打开雪球APP
        2、点击搜索输入框
        3、向搜索输入框里输入：阿里巴巴
        4、在搜索结果里选择阿里巴巴，然后点击
        5、获取阿里巴巴股票的价格，并判断这只股票的价格>200
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"title_container")]//*[@text="股票"]').click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        # current_price = float(self.driver.find_element(*locator).text)
        # current_price = float(self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        current_price = float(WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator).text))
        assert current_price > 200

    def test_search2(self):
        search_element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_element.text)
        print(search_element.location)
        print(search_element.size)
        if search_element.is_displayed():
            search_element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba_element = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            # alibaba_element.is_displayed()
            if alibaba_element.get_attribute("displayed") == "true":
                print('搜索成功')
            else:
                print('搜索失败')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()  # [100%]{'width': 1170, 'height': 1872, 'x': 0, 'y': 0}
        width = window_rect['width']
        height = window_rect['height']
        # action.press(x=515,y=1518).wait(600).move_to(x=515,y=322).release().perform()  # 不建议使用
        action.press(x=width / 2, y=height * 4 / 5).wait(500).move_to(x=width / 2, y=height * 1 / 5).release().perform()

    # UIAutomator定位
    def test_myinfo(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('chenshifeng001')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('chenshifeng001')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("二马由之").'
                                                        'instance(0));').click()

    def test_toast(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').click()
        TouchAction(self.driver).press(x=515, y=322).wait(600).move_to(x=515, y=1518).release().perform()
        print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"更新")]')

    def test_get_attribute(self):
        search_element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_element.get_attribute('content-desc'))
        print(search_element.get_attribute('resource-id'))
        print(search_element.get_attribute('enabled'))
        print(search_element.get_attribute('clickable'))
        print(search_element.get_attribute('bounds'))

    @pytest.mark.parametrize('searchkey,type,price', [
        ['alibaba', 'BABA', 308],
        ['xiaomi', '01810', 21]
    ])
    def test_param_search(self, searchkey, type, price):
        '''
        1、打开雪球APP
        2、点击搜索输入框
        3、向搜索输入框里输入：阿里巴巴 or 小米
        4、在搜索结果里选择第一个，然后点击
        5、获取所选股票的价格，并判断这只股票的价格
        :return:
        '''
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        current_price = self.driver.find_element(MobileBy.XPATH,
                                                 f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        current_price = float(current_price)
        expect_price = price
        expect_price = float(expect_price)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
