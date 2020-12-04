#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:conftest.py
@time:2020/12/04
"""
# 钩子函数，解决中文用例名称显示乱码
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")