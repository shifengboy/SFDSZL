#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:adress_list_page.py
@time:2020/11/01

通讯录tab
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    def click_addmember(self):
        self.find_and_click(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                          '.scrollable(true).instance(0))'
                                                          '.scrollIntoView(new UiSelector().textContains("添加成员")'
                                                          '.instance(0));')
        return MemberInviteMenuPage(self.driver)

    def click_member_manager(self):
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxr')
        return self

    def close_member_manager(self):
        self.wait_click(15, MobileBy.ID, 'com.tencent.wework:id/hxm')
        # self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxm')
        return self

    def click_delete_member(self, name):

        self.wait_click(15, MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                          '.scrollable(true).instance(0))'
                                                          f'.scrollIntoView(new UiSelector().textContains("{name}")'
                                                          '.instance(0));')

        self.find_and_click(MobileBy.XPATH, f'//*[@text="{name}"]')

        from app.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def search_member(self, name):
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxw')
        self.find_and_sendkeys(MobileBy.ID, 'com.tencent.wework:id/ghu', name)
        return self.find(MobileBy.ID, 'com.tencent.wework:id/ca0').text  # 无搜索结果
