#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_demo.py
@time:2021/03/07
"""
import pytest


def test_success_demo():
    assert 1 == 1


def test_fail_demo():
    assert 1 == 2


def test_skip_demo():
    assert pytest.skip("skip")


@pytest.mark.parametrize('a,b,result', [
    [1, 1, 2],
    [2, 2, 3],
    [3, 4, 7]
])
def test_params(a, b, result):
    assert result == a + b
