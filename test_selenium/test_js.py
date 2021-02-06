#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_js.py
@time:2020/10/17
"""
from time import sleep

from test_selenium.base import Base


class TestJS(Base):
    # 百度搜索演示
    def test_js(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()  # 点击搜索
        sleep(2)
        self.driver.execute_script('document.documentElement.scrollTop=10000')  # 页面向下滑动10000个像素
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()  # 点击下一页
        sleep(2)
        self.driver.execute_script('document.documentElement.scrollTop=10000')  # 页面向下滑动10000个像素
        sleep(2)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))
        # JSON.stringify() 方法用于将 JavaScript 值转换为 JSON 字符串。
        # performance.timing  加载和使用当前页面期间发生的各种事件的性能计时信息。

    def test_modify_traindate(self):
        # 12306时间选择框演示
        self.driver.get('https://www.12306.cn/index/')
        sleep(2)
        # 通过js代码设置时间（需先去除readonly属性）
        self.driver.execute_script(
            'a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="2020-12-31"')
        sleep(2)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
