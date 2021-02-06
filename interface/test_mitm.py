#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_mitm.py
@time:2020/11/29
"""
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 增加请求的头信息
    flow.request.headers["myheader"] = "shifeng"
    print(flow.request.headers)
