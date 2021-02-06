#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:baseapi.py
@time:2020/12/06
"""
import json

import requests


class BaseApi:
    params = {}
    def __init__(self, corpid, corpsecret):
        self.token = self.get_token(corpid, corpsecret)

    def get_token(self, corpid, corpsecret):
        # r = requests.get(
        #     'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        #     params={'corpid': corpid, 'corpsecret': corpsecret})
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        return r.json()["access_token"]

    def send(self, kwargs):
        data = json.dumps(kwargs)
        for key,value in self.params.items():
            data = data.replace("${"+key+"}",value)
        kwargs = json.loads(data)
        r = requests.request(**kwargs)
        return r
