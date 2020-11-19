#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:app.py
@time:2020/11/19

app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，登录App，进入到首页
"""
import yaml
from appium import webdriver

from dingding.page.base_page import BasePage
from dingding.page.main_page import MainPage

with open('../config/appconfig.yml') as f:
    datas = yaml.safe_load(f)
    desired_caps = datas['desired_caps']
    ip = datas['ip']


class APP(BasePage):
    def start(self):
        if self.driver is None:
            self.driver = webdriver.Remote(f'http://{ip}/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def login(self):
        MainPage(self.driver).login()

    def restart(self):
        pass

    def stop(self):
        pass

    def close(self):
        pass

    def goto_main_page(self):
        return MainPage(self.driver)
