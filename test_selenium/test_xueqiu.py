#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_xueqiu.py
@time:2020/10/24
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueQiu:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "automationName": "Appium",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "appActivity": ".common.MainActivity",
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
        # self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]") \
        #     .click()
        # self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[1]") \
        #     .click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 200

    def test_search2(self):
        search_element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_element.text)
        print(search_element.location)
        print(search_element.size)
        if search_element.is_displayed():
            search_element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba_element = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            # alibaba_element.is_displayed()
            if alibaba_element.get_attribute("displayed") == "true":
                print('搜索成功')
            else:
                print('搜索失败')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=515,y=1518).wait(600).move_to(x=515,y=322).release().perform()

