#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_main.py
@time:2020/11/08
"""
from frame.main_page import Main


class TestMain:

    def test_main(self):
        Main().goto_market().goto_search().search()