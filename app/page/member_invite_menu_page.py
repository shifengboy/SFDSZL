#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:member_invite_menu_page.py
@time:2020/11/

添加成员页菜单页
"""
from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    def click_manual_menu(self):
        self.find_and_click(MobileBy.XPATH,'//*[contains(@text,"手动输入添加")]')
        from app.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_toast(self):
        return self.get_toast_text(MobileBy.XPATH,'//*[@class="android.widget.Toast"]')
        # return self.find(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text

