#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_report.py
@time:2021/01/27
"""
class TestReport:

    def test_one(self):
        x = "shifeng"
        assert "feng" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"


