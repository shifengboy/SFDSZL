#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:add_member_page.py
@time:2020/11/01

添加成员页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self,name,gender,phonenu):
        # 设置 【用户名】【性别】【手机号】
        self.find_and_sendkeys(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText',name)
        if gender == '女':
            self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"男")]')
            self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"女")]')
        else:
            self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"男")]')
            self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"男")]')

        self.find_and_sendkeys(MobileBy.XPATH, '//*[@text="手机号"]',phonenu)
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
