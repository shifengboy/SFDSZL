#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_gooffwork.py
@time:2020/11/19
@case：钉钉下班打卡
"""
from dingding.page.app import APP


class TestGoOffWork:

    def setup(self):
        self.app = APP()

        # 登录处理
        try:
            self.app.login()
        except Exception:
            pass

        self.page = self.app.goto_main_page()

    def test_gooffwork(self):
        self.page.goto_workbench().chose_company().clock_out()
        assert '打卡成功' in self.page.get_pagesource()
