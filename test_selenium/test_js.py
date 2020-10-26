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
    def test_js(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(2)
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(2)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    def test_modify_traindate(self):
        self.driver.get('https://www.12306.cn/index/')
        sleep(2)
        self.driver.execute_script(
            'a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="2020-12-31"')
        sleep(2)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
