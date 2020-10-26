#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_alert.py
@time:2020/10/18
"""
from time import sleep
from selenium.webdriver import ActionChains
from test_selenium.base import Base

class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drag=self.driver.find_element_by_id('draggable')
        drop=self.driver.find_element_by_id('droppable')
        ActionChains(self.driver).drag_and_drop(drag,drop).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()    # 接受警告框
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(2)