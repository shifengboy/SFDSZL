#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_weixin.py
@time:2020/10/25
"""
from test_web.test_demo.index_page import IndexPage


class TestWeiXin:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        # assert self.index.goto_login().goto_register().register()
        assert self.index.goto_register().register()

