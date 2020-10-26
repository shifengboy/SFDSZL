#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_severity.py
@time:2020/10/11
"""
import allure
import pytest


# 不加任何标记,默认normal
def test_with_no_severity():
    pass


# trivial:不重要，轻微缺陷（必输项无提示，或者提示不规范）
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


# minor 级别 不太重要，次要缺陷（界面错误与UI需求不符）
@allure.severity(allure.severity_level.MINOR)
def test_with_minor_severity():
    pass


# normal:正常问题，普通缺陷（数值计算错误）
@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


# critical:严重，临界缺陷（功能点缺失）
@allure.severity(allure.severity_level.CRITICAL)
def test_with_ritical_severity():
    pass


# blocker:阻塞，中断缺陷（客户端程序无响应，无法执行下一步操作）
@allure.severity(allure.severity_level.BLOCKER)
def test_with_blocker_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    # 不加任何标记，默认为同class级别
    def test_inside_with_normal_severity(self):
        pass

    # 重新设置了critical级别
    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_with_critical_severity(self):
        pass
