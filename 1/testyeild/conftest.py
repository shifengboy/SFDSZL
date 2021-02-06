#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:conftest.py
@time:2020/12/31
"""
import pytest


@pytest.fixture(scope='module', autouse=True)
def case_before():
    print("brfore yeild")
    yield

    print("after yield")
