#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_maplocal.py
@time:2020/11/29
"""
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 打开保存在本地的数据文件
        with open("/Users/chenshifeng/MyCode/PythonCode/SFDSZL/interface/quote.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中数据作为返回内容
                f.read(),
                # 指定返回数据的类型
                {"Content-Type": "application/json"}  # (optional) headers
            )