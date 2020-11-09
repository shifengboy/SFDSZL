#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:base_page.py
@time:2020/11/08
"""
import logging

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from frame.handle_black import handle_black

with open('./base_page.yml') as f:
    datas = yaml.safe_load(f)
    desired_caps = datas['desired_caps']
    ip = datas['ip']


class BasePage:
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{root_logger.handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    black_list = [(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]
    max_num = 3
    err_num = 0

    def __init__(self, driver: WebDriver = None):
        '''
        初始化应用
        '''

        if driver is None:
            self.driver = webdriver.Remote(f'http://{ip}/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None) -> WebElement:
        '''
        查找元素
        :param by:
        :param locator:
        :return:
        '''
        logging.info(f'find.by:{by}')
        logging.info(f'find.locator:{locator}')
        if locator is None:
            result = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(*by))
        else:
            result = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))

        return result

    def parse_yaml(self, path, func_name):
        logging.info(f'parse_yaml.path:{path}')
        logging.info(f'parse_yaml.func_name:{func_name}')
        with open(path, encoding='UTF-8') as f:
            datas = yaml.safe_load(f)
            # print(datas[func_name])
            self.parse(datas[func_name])

    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['loactor']).click()
            elif 'send_keys' == step['action']:
                self.find(step['by'], step['loactor']).send_keys(step['content'])

