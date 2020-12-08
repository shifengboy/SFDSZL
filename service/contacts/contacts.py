#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:contacts.py
@time:2020/12/08
"""
import json
import random

from service.baseapi import BaseApi


class Contacts(BaseApi):
    def __init__(self, corpid, corpsecret):
        super(Contacts, self).__init__(corpid, corpsecret)

    def phoneNORandomGenerator(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    def add(self, userid, name, **kwargs):
        data = {
            'method': 'POST',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create',
            'params': {'access_token': self.token},
            'json': {
                "userid": userid,
                "name": name,
                **kwargs
            }
        }
        print(data)
        r = self.send(data)
        print('add log:', json.dumps(r.json(), indent=2))
        return r

    def add_and_detect(self, userid, name, **kwargs):
        r = self.add(userid, name, **kwargs)
        # 手机号码已存在
        if r.json()['errcode'] == 60104:
            kwargs['mobile'] = self.phoneNORandomGenerator()
            r = self.add_and_detect(userid, name, **kwargs)
        # UserID已存在
        if r.json()['errcode'] == 60102:
            self.delete(userid)
            r = self.add_and_detect(userid, name, **kwargs)
        return r

    def select(self, userid):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'params': {'access_token': self.token, 'userid': userid},
        }
        r = self.send(data)
        print('select log:', json.dumps(r.json(), indent=2))
        return r

    def update(self, userid, **kwargs):
        data = {
            'method': 'POST',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/update',
            'params': {'access_token': self.token},
            'json': {
                "userid": userid,
                **kwargs
            }
        }
        r = self.send(data)
        print('update log:', json.dumps(r.json(), indent=2))
        return r

    def update_and_detect(self,userid, **kwargs):
        r = self.update(userid, **kwargs)
        # 员工不存在
        if r.json()['errcode'] == 60111:
            name = ''.join([chr(random.randint(0x4e00, 0x9fbf)) for i in range(3)])
            mobile = self.phoneNORandomGenerator()
            self.add_and_detect(userid, name,mobile=mobile, department=[2],**kwargs)
            r = self.update_and_detect(userid, **kwargs)
        return r


    def delete(self, userid):
        data = {
            'method': 'GET',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            'params': {'access_token': self.token, 'userid': userid}
        }
        r = self.send(data)
        print('update log:', json.dumps(r.json(), indent=2))
        return r

    def delete_and_detect(self,userid):
        r = self.delete(userid)
        # 员工不存在
        if r.json()['errcode'] == 60111:
            name = ''.join([chr(random.randint(0x4e00, 0x9fbf)) for i in range(3)])
            mobile = self.phoneNORandomGenerator()
            self.add_and_detect(userid, name, mobile=mobile, department=[2])
            r = self.delete_and_detect(userid)
        return r

    def batchdelete(self, useridlist):
        data = {
            'method': 'POST',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete',
            'params': {'access_token': self.token},
            'json': {
                "useridlist": useridlist
            }
        }
        r = self.send(data)
        print('update log:', json.dumps(r.json(), indent=2))
        return r
