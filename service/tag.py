#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:tag.py
@time:2020/12/03
"""
import json
from typing import List

import requests
from jsonpath import jsonpath


class Tag:

    def __init__(self, corpid, corpsecret):
        self.token = self.get_token(corpid, corpsecret)

    def get_token(self, corpid, corpsecret):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret})
        return r.json()["access_token"]

    # 根据group_name获取get_group_id
    def get_group_id(self, group_name=None):

        # 若标签组为空，返回所有标签组id
        if group_name is None or group_name == '':
            r = self.list()
            # print(json.dumps(r.json(), indent=2))
            return jsonpath(r.json(), "$..group_id")
        else:
            r = self.list()
            return jsonpath(r.json(), f"$..[?(@.group_name=='{group_name}')]")[0]['group_id']

    # 根据tag_name获取get_group_id
    def get_tag_id(self,tag_name):
        r = self.list()
        return jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['id']

    def get_tag_ids(self,*tag_name):
        ids = []
        print(tag_name)
        r = self.list()
        for name in tag_name:
            print(name)
            id = jsonpath(r.json(), f"$..[?(@.name=='{name}')]")[0]['id']
            ids.append(id)
        return ids

    def add(self, tag_name, tag_order=None, group_id=None, group_name=None, order=None):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                "group_id": group_id,
                "group_name": group_name,
                "order": order,
                "tag": [{
                    "name": tag_name,
                    "order": tag_order
                }
                ]
            }
        )
        # print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={'tag_id': []},
        )

        # print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={'access_token': self.token},
            json={
                "id": id,
                "name": tag_name,
            }
        )
        # print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, tag_id: List = None, group_id: List = None):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={
                "tag_id": tag_id,
                "group_id": group_id
            }
        )
        # print(json.dumps(r.json(), indent=2))
        return r
