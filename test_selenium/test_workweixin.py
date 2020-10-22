#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_workweixin.py
@time:2020/10/22
"""
import shelve
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from test_selenium.base import Base


class TestWorkWeiXin(Base):
    '''企业微信测试case'''

    def test_work_winxin_login(self):
        '''使用cookie登录企业微信'''
        db = shelve.open("cookies")
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def test_work_winxin_import_address_book(self):
        '''上传文件导入通讯录'''
        # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "/Users/chenshifeng/Downloads/通讯录批量导入模板.xlsx")
        # 验证 上传文件名   ww_fileImporter_fileContainer_fileNames
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "通讯录批量导入模板.xlsx" == filename
        sleep(3)
