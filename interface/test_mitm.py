#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_mitm.py
@time:2020/11/29
"""
# from mitmproxy import http


# def request(flow: http.HTTPFlow):
#     # 增加请求的头信息
#     flow.request.headers["myheader"] = "shifeng"
#     print(flow.request.headers)

from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]