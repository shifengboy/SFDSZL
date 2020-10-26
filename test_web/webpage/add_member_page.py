#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:add_member_page.py
@time:2020/10/25
"""
from selenium.webdriver.common.by import By

from test_web.webpage.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    # 添加联系人
    def add_member(self, username, account, phonenum):
        self.find(By.CSS_SELECTOR, "#username").send_keys(username)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(account)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phonenum)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return True

    def get_member(self, value):
        # 验证联系人添加成功
        # contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # titlelist = [element.get_attribute("title") for element in contactlist]
        # print(titlelist)
        # titlelist = []
        # for element in contactlist:
        #     titlelist.append(element.get_attribute("title"))
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                return True
            total_list = total_list + titlelist

            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list