#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2020/11/01
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.adress_list_page import AddressListPage
from app.page.base_page import BasePage


class MainPage(BasePage):
    def go_message(self):
        '''
        进入消息tab（默认tab）
        :return:
        '''
        pass
    def go_address_list(self):
        '''
        通讯录tab
        :return:
        '''
        self.find_and_click(MobileBy.XPATH,'//*[contains(@text,"通讯录")]')
        return AddressListPage(self.driver)
    def go_workbench(self):
        '''
        工作台tab
        :return:
        '''
        pass
    def go_my(self):
        '''
        我tab
        :return:
        '''
        pass