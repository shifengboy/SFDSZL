#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2020/11/19
@tip：由于我们只需部分功能，故本次把所有所需功能都放入本页面内，不做多个页面的封装
"""
from dingding.base_page import BasePage


class MainPage(BasePage):
    def goto_workbench(self):
        self.parse_yaml('./main_page.yml', 'goto_workbench')
        return self

    def chose_company(self):
        self.parse_yaml('./main_page.yml', 'chose_company')
        return self

    def goto_attendance(self):
        self.parse_yaml('./main_page.yml', 'goto_attendance')
        return self

    def clock_in(self):
        self.parse_yaml('./main_page.yml', 'clock_in')

    def clock_out(self):
        self.parse_yaml('./main_page.yml', 'clock_out')
