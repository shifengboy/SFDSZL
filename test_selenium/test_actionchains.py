#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_actionchains.py
@time:2020/09/27
"""

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestDefaultSuite():
    def setup_method(self ):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
        pass

        # 鼠标点击测试
        # @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        click_btn = self.driver.find_element_by_xpath('//input[@value="click me"]')  # 单击按钮
        doubleclick_btn = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')  # 双击按钮
        rightclick_btn = self.driver.find_element_by_xpath('//input[@value="right click me"]')  # 右键单击按钮

        # action=ActionChains(self.driver)
        # action.click(click_btn)  # 单击
        # action.double_click(doubleclick_btn)  # 双击
        # action.context_click(rightclick_btn)  # 右键
        # action.perform()
        # sleep(5)

        # 或者直接以长链的方式执行，按照顺序依次执行
        ActionChains(self.driver).click(click_btn).double_click(doubleclick_btn).context_click(
            rightclick_btn).perform()

    # 鼠标移动测试
    def test_case_move(self):
        # self.driver.get('https://www.baidu.com/')
        # set_ele=self.driver.find_element_by_id('s-usersetting-top')  # 百度的设置元素
        # ActionChains(self.driver).move_to_element(set_ele).perform()
        # sleep(5)
        self.driver.get('http://sahitest.com/demo/mouseover.htm')
        write = self.driver.find_element_by_xpath(
            '//input[@value="Write on hover"]')  # 鼠标移动到此元素，在下面的input框中会显示“Mouse moved”
        blank = self.driver.find_element_by_xpath('//input[@value="Blank on hover"]')  # 鼠标移动到此元素，会清空下面input框中的内容
        result = self.driver.find_element_by_name('t1')
        action = ActionChains(self.driver)
        action.move_to_element(write).perform()  # 移动到write，显示“Mouse moved”
        print(result.get_attribute('value'))
        # action.move_to_element(blank).perform()
        action.move_by_offset(10, 50).perform()  # 移动到距离当前位置(10,50)的点，与上句效果相同，移动到blank上，清空
        print(result.get_attribute('value'))
        action.move_to_element_with_offset(blank, 10, -40).perform()  # 移动到距离blank元素(10,-40)的点，可移动到write上
        print(result.get_attribute('value'))
        sleep(2)

    # 鼠标拖拽
    def test_case_drapdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        dragger = self.driver.find_element_by_id('dragger')  # 被拖拽元素
        item1 = self.driver.find_element_by_xpath('//div[text()="Item 1"]')  # 目标元素1
        item2 = self.driver.find_element_by_xpath('//div[text()="Item 2"]')  # 目标2
        item3 = self.driver.find_element_by_xpath('//div[text()="Item 3"]')  # 目标3
        item4 = self.driver.find_element_by_xpath('//div[text()="Item 4"]')  # 目标4

        action = ActionChains(self.driver)
        action.drag_and_drop(dragger, item1).perform()  # 1.移动dragger到目标1
        sleep(2)
        action.click_and_hold(dragger).release(item2).perform()  # 2.效果与上句相同，也能起到移动效果
        sleep(2)
        action.click_and_hold(dragger).move_to_element(item3).release().perform()  # 3.效果与上两句相同，也能起到移动的效果
        sleep(2)
        # action.drag_and_drop_by_offset(dragger, 400, 150).perform()  # 4.移动到指定坐标
        action.click_and_hold(dragger).move_by_offset(400, 150).release().perform()  # 5.与上一句相同，移动到指定坐标
        sleep(2)


    def test_key(self):
        self.driver.get('https://www.baidu.com/')
        # dom = self.driver.find_element_by_id('kw')
        #
        # ActionChains(self.driver).key_down(Keys.SHIFT, dom).send_keys('a').send_keys('c').key_up(Keys.SHIFT).pause(2).perform()

        e1 = self.driver.find_element_by_id('s-usersetting-top')

        ActionChains(self.driver).click_and_hold(e1).perform()
        self.driver.find_element_by_xpath('//*[@class="setpref"]').click()

        sleep(5)




