#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_tag.py
@time:2020/12/03
"""
import json
import time

import pytest
from jsonpath import jsonpath

from service.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag(corpid='ww1f67d03559842a74', corpsecret='qHoLjOXpHxtHp5ZtXOB8_IOpmywjRK9QGChKaSeBd6A')

    @pytest.mark.parametrize('group_id,tag_name', [
        ['et2SSvCwAA9YjLT24Z5wnioBonvsUzHg', 'test_add'],
        ['et2SSvCwAA9YjLT24Z5wnioBonvsUzHg', 'test_add_中文'],
        ['et2SSvCwAA9YjLT24Z5wnioBonvsUzHg', 'test_add—@#￥%']
    ])
    def test_tag_add(self, group_id, tag_name):
        self.tag.add(tag_name=tag_name, group_id=group_id)
        r = self.tag.list()
        assert tag_name in jsonpath(r.json(), "$..name")

    @pytest.mark.parametrize('tag_id,tag_name', [
        ['et2SSvCwAAr1QOCTeqvm863zythp_hDA', 'test1_new_'],
        ['et2SSvCwAAr1QOCTeqvm863zythp_hDA', 'test1_new_中文_']
    ])
    def test_tag_update(self, tag_id, tag_name):
        # group_name = 'testapi'
        tag_name = tag_name + time.strftime('%Y%m%d_%H%M')
        self.tag.list()
        self.tag.update(id=tag_id, tag_name=tag_name)
        r = self.tag.list()

        # tags = [
        #         tag
        #         for group in r.json()['tag_group'] if group['group_name'] == group_name
        #         for tag in group['tag'] if tag['name'] == tag_name
        # ]
        # assert tags != []
        # print(jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]"))
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    @pytest.mark.parametrize('tag_id', [
        [['et2SSvCwAAMa8-pa2mj3fy2XN2Ij6vnQ','et2SSvCwAA2eKB2rn7v3I9bzUCGM-rKQ']]
    ])
    def test_tag_delete(self,tag_id):
        self.tag.delete(tag_id=tag_id)
        r = self.tag.list()
        print(json.dumps(r.json(), indent=2))
        assert not jsonpath(r.json(), f"$..[?(@.name=='{tag_id}')]")


