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

from service.baseapi import BaseApi


class Tag(BaseApi):

    def __init__(self, corpid, corpsecret):
        super(Tag, self).__init__(corpid, corpsecret)

    # 根据group_name获取get_group_id
    def get_group_id(self, group_name):
        r = self.list()
        # return jsonpath(r.json(), f"$..[?(@.group_name=='{group_name}')]")[0]['group_id']
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return group['group_id']
        raise ValueError('该标签组不存在')

    def get_group_ids(self):
        '''
        :return: 返回所有标签组id
        '''
        r = self.list()
        return jsonpath(r.json(), "$..group_id")

    def get_tag_id(self, tag_name):
        r = self.list()
        # return jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['id']
        for group in self.list().json()['tag_group']:
            for tag in group['tag']:
                if tag_name in tag['name']:
                    return tag['id']
        return False

    # 根据tag_name获取get_group_id
    def get_tag_ids(self, tag_name: List):
        r = self.list()
        # return jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['id']
        ids = []
        for name in tag_name:
            for group in self.list().json()['tag_group']:
                for tag in group['tag']:
                    if name in tag['name']:
                        ids.append(tag['id'])
        return ids

    def add(self, tag_name=None, tag=None, tag_order=None, group_id=None, group_name=None, order=None, **kwargs):
        if tag is None:
            json_data = {
                "group_id": group_id,
                "group_name": group_name,
                "order": order,
                "tag": [{
                    "name": tag_name,
                    "order": tag_order
                }]
            }
        else:
            json_data = {
                "group_id": group_id,
                "group_name": group_name,
                "order": order,
                "tag": tag
            }
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'params': {'access_token': self.token},
            'json': json_data
        }
        r = self.send(data)

        print('add log:', json.dumps(r.json(), indent=2))
        return r

    def add_and_detect(self, group_name, tag, **kwargs):
        r = self.add(group_name=group_name, tag=tag, **kwargs)
        # 如果添加的元素已经存在地
        if r.json()["errcode"] == 40071:
            group_id = self.get_group_id(group_name)
            if not group_id:
                # 元素不在，接口有问题
                return ""
            self.delete(group_id=[group_id])
            self.add(group_name=group_name, tag=tag, **kwargs)
        result = self.get_group_id(group_name)
        if not result:
            print("add not success")
        return result

    def is_group_name_exist(self, group_name):
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return True
        return False

    def is_group_id_exist(self, group_id):
        # 查询元素是否存在，如果不存在，报错
        for group in self.list().json()["tag_group"]:
            if group_id in group["group_id"]:
                return True
        print("group id not in goup")
        return False

    def list(self):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'params': {'access_token': self.token},
            'json': {'tag_id': []}
        }
        # print(json.dumps(r.json(), indent=2))
        r = self.send(data)
        return r

    def update(self, id, tag_name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'params': {'access_token': self.token},
            'json': {
                "id": id,
                "name": tag_name,
            }
        }
        # print(json.dumps(r.json(), indent=2))
        r = self.send(data)
        return r

    def delete(self, tag_id: List = None, group_id: List = None):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token},
            'json': {
                "tag_id": tag_id,
                "group_id": group_id
            }
        }
        r = self.send(data)
        print('delete log:', json.dumps(r.json(), indent=2))
        return r

    def delete_and_detect(self, tag_id: List = None, group_id: List = None):
        r = self.delete(tag_id, group_id)
        if r.json()["errcode"] == 40068:
            pass

    def delete_and_detect_group(self, group_ids):
        deleted_group_ids = []
        r = self.delete(group_id=group_ids)
        if r.json()["errcode"] == 40068:
            # 如果标签不存在，就添加一个标签，将它的 group_id 存储进来
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_id_tmp = self.add_and_detect(group_name="TMP00123",
                                                       tag=[{"name": "TAG1"}])
                    deleted_group_ids.append(group_id_tmp)
                # 如果标签存在，就将它存入标签组
                else:
                    deleted_group_ids.append(group_id)
            r = self.delete(group_id=deleted_group_ids)
        return r
