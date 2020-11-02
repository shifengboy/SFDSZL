#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:base_page.py
@time:2020/11/01

base_page.py 基类模块：主要用于初始化driver, 定义find, 常用的最基本的方法
"""
import logging
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{root_logger.handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info('find_and_click')
        return self.find(by, locator).click()

    def wait_click(self,timeout, by, locator):
        logging.info('wait_click')
        return WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable((by, locator))).click()

    def find_and_sendkeys(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def get_toast_text(self,by, locator):
        logging.info('get_toast_text')
        return self.find(by, locator).text
