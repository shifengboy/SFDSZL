#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_frame.py
@time:2020/10/17
"""
from test_selenium.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        # self.driver.switch_to_frame('iframeResult')  # 该方法已逐渐被废弃，不建议使用
        print(self.driver.find_element_by_id('draggable').text)
        self.driver.switch_to.parent_frame()  # 切换回父frame
        # self.driver.switch_to.default_content() # 切换回主文档
        print(self.driver.find_element_by_id('submitBTN').text)