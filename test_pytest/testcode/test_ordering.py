#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_ordering.py
@time:2020/09/16
"""
import pytest

# @pytest.mark.dependency()
def test_01():
    assert False

@pytest.mark.dependency(depends=["test_01"])
def test_02():
    print("执行测试2")

