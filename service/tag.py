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


class Tag:

    def __init__(self, corpid, corpsecret):
        self.token = self.get_token(corpid, corpsecret)

    def get_token(self, corpid, corpsecret):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret})
        return r.json()["access_token"]

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
