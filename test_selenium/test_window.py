#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_window.py
@time:2020/10/17
"""
'''
实现百度注册及登录功能（部分功能）
1、打开百度首页，点击登录
2、点击立即注册，跳转到新页面
3、切换到新页面，输入用户名及密码开始注册
4、切换回登录页面，进行登录
'''
from time import sleep
from test_selenium.base import Base

class TestWindow(Base):
    def test_window(self):
        self.driver.get('https:www.baidu.com')
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)  # 当前窗口
        print(self.driver.window_handles)  # 当前窗口
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])   # 切换窗口
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys(18888888888)
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('123456')
        sleep(2)
        self.driver.switch_to_window(windows[0])  # 切换回窗口
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('123456')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(2)