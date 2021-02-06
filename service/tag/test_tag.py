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

from service.tag.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag(corpid='ww1f67d03559842a74', corpsecret='qHoLjOXpHxtHp5ZtXOB8_IOpmywjRK9QGChKaSeBd6A')

    @pytest.mark.parametrize('group_name,tag_name', [
        ['testapi', 'test_add'],
        ['testapi', 'test_add_中文'],
        ['testapi', 'test_add—@#￥%']
    ])
    def test_tag_add(self, group_name, tag_name):
        r = self.tag.add(tag_name=tag_name, group_name=group_name)
        # assert tag_name in jsonpath(r.json(), "$..name")
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_add_and_detect(self):
        group_name = "TMP00123"
        tag = [
            {"name": "TAG1"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]
        r = self.tag.add_and_detect(group_name, tag)
        assert r

    @pytest.mark.parametrize('tag_name,tag_name_new', [
        ['${tag_name}', 'test_add_haha'],
        # ['test_add_中文', 'test_add_中文_new1']
    ])
    def test_tag_update(self, tag_name, tag_name_new):
        '''
        :param tag_name: 要修改的标签名
        :param tag_name_new: 修改后的标签名
        :return:
        '''
        tag_id = self.tag.get_tag_id(tag_name)
        self.tag.update(id=tag_id, tag_name=tag_name_new)
        r = self.tag.list()
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name_new}')]")[0]['name'] == tag_name_new

    @pytest.mark.parametrize('tag_name', [
        'TAG3',
        'test_add_中文_new1'
    ])
    def test_tag_delete(self, tag_name):
        tag_id = self.tag.get_tag_id(tag_name)
        if tag_id:
            r = self.tag.delete(tag_id=[tag_id])
            assert r.json()['errcode'] == 0
        else:
            raise ValueError('标签不存在')

    def test_group_delete(self):
        self.tag.delete(group_id=['et2SSvCwAAdVFD90fa-8wbnbQygW2brA'])
        r = self.tag.list()
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["et_6ElDwAAyvuY_HFzh0vHvy-yqYhVHA"])
        assert r.json()["errcode"] == 0



    # 数据清理,可清理指定标签组，若未指定，则清除所有
    # @pytest.mark.skip
    @pytest.mark.parametrize('group_name', [
        # 'TMP00123'
        ''
    ])
    def test_tag_clean(self, group_name):

        # 标签组为空，清除所有标签
        if group_name is None or group_name == '':
            group_ids = self.tag.get_group_ids()
            self.tag.delete(group_id=group_ids)
            r = self.tag.list()
            assert not jsonpath(r.json(), "$..group_name")
        else:
            try:
                group_id = self.tag.get_group_id(group_name)
            except:
                print("要清除的标签组不存在或已清除")
            else:
                self.tag.delete(group_id=group_id)
                r = self.tag.list()
                # print(json.dumps(r.json(), indent=2))
                assert not jsonpath(r.json(), f"$..[?(@.group_name=='{group_name}')]")
