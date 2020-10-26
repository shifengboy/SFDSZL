#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2020/10/25
"""
from selenium.webdriver.common.by import By
from test_web.webpage.add_member_page import AddMemberPage
from test_web.webpage.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     self.driver.implicitly_wait(5)

    # 添加联系人
    def goto_addmember(self):
        # 直接在首页点击【添加联系人】
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        # 点击 【联系人】
        self.find(By.CSS_SELECTOR,'#menu_contacts').click()
        # 点击 【添加联系人】按钮
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        self.wait_for_click((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")).click()


        '''
        # 点击 【添加联系人】按钮
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")

        # element:WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element = self.wait_for_click(locator)
        # element.click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)
        '''
        return AddMemberPage(self.driver)
