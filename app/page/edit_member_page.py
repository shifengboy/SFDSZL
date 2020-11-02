#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:edit_member_page.py
@time:2020/11/02
"""
from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage


class EditMemberPage(BasePage):
    def delete_member(self):
        # self.find_and_click(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
        #                                                   '.scrollable(true).instance(0))'
        #                                                   '.scrollIntoView(new UiSelector().text("删除成员")'
        #                                                   '.instance(0));')

        self.find_and_click(MobileBy.ID,'com.tencent.wework:id/eh7')   #删除成员

        self.find_and_click(MobileBy.XPATH, '//*[@text="确定"]')
        from app.page.adress_list_page import AddressListPage
        return AddressListPage(self.driver)

