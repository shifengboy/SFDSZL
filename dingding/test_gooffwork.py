#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_gooffwork.py
@time:2020/11/19
@case：钉钉下班打卡
"""
from dingding.main_page import MainPage


class TestGoOffWork:
    def setup(self):
        self.page = MainPage()

    def test_gooffwork(self):
        self.page.goto_workbench().chose_company().clock_out()
        assert '打卡成功' in self.page.get_pagesource()
