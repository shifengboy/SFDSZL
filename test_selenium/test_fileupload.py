#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_fileupload.py
@time:2020/10/18
"""
from time import sleep
from test_selenium.base import Base


class TestFileUpload(Base):
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        sleep(2)
        self.driver.find_element_by_id('stfile').send_keys('/Users/chenshifeng/Desktop/photo.png')
        sleep(5)
