#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_classic.py
@time:2020/12/02
"""
import json
import time

import requests
from jsonpath import jsonpath

# todo: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# todo: 代码冗余，需要封装
# todo: 无法清晰的描述业务
# todo: 使用jsonpath表达更灵活的递归查找
def test_tag_list():
    corpid = 'ww1f67d03559842a74'
    corpsecret = 'qHoLjOXpHxtHp5ZtXOB8_IOpmywjRK9QGChKaSeBd6A'
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret})
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    token = r.json()['access_token']

    tag_name = 'test1_new' + time.strftime('%Y%m%d_%H%M')
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={'access_token': token},
        json = {
            "id": "et2SSvCwAAr1QOCTeqvm863zythp_hDA",
            "name": tag_name,
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token': token},
        # json={'tag_id':['etXXXXXXXXXX','etYYYYYYYYYY']},
        # data={
        #     "tag_id": [
        #         "etXXXXXXXXXX",
        #         "etYYYYYYYYYY"
        #     ]
        # }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    # for group in  r.json()['tag_group']:
    #     if group['group_name'] == 'testapi':
    #         for tag in group['tag']:
    #             if tag['name'] == 'test1_new':
    #                 print('ok')
    tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == 'testapi'
            for tag in group['tag'] if tag['name'] == tag_name
    ]
    # jsonpath(f"$..[?(@.name='{tag_name}')]")
    assert tags != []


