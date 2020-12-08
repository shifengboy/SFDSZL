#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_contacts.py
@time:2020/12/08
"""
import pytest

from service.contacts.contacts import Contacts


class TestContacts:
    def setup_class(self):
        self.contacts = Contacts(corpid='ww1f67d03559842a74', corpsecret='MWWjmNT5os8U0uYMIWqL2DnU8ziiejJFR5B2Bu866zw')

    @pytest.mark.parametrize('userid,name,mobile,department', [
        ['laodeng001', '老邓001', '+86 13110000001',[2]],
        ['laodeng002', '老邓002', '+86 13100000002',[2]],
        ['laodeng003', '老邓003', '+86 13100000003',[2]]
    ])
    def test_add(self, userid, name, mobile,department):
        r = self.contacts.add(userid, name, mobile=mobile,department=department)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'created'


    @pytest.mark.parametrize('userid', [
        'laodeng001'
    ])
    def test_select(self,userid):
        r = self.contacts.select(userid)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'ok'

    def test_update(self):
        r = self.contacts.update('laodeng001',gender=2)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'updated'

    def test_delete(self):
        r = self.contacts.delete('laodeng003')
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'deleted'

    def test_batchdelete(self):
        r = self.contacts.batchdelete(['laodeng001','laodeng002'])
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'deleted'

    @pytest.mark.parametrize('userid,name,mobile,department', [
        ['laodeng001', '老邓001', '+86 13110000001',[2]],
        ['laodeng002', '老邓002', '+86 13100000002',[2]],
        ['laodeng003', '老邓003', '+86 13100000003',[2]]
    ])
    def test_add_and_detect(self, userid, name, mobile,department):
        r = self.contacts.add_and_detect(userid, name, mobile=mobile,department=department)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'created'

    def test_update_and_detect(self):
        r = self.contacts.update_and_detect('laodeng006',gender=2)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'updated'

    def test_delete_and_detect(self):
        r = self.contacts.delete_and_detect('laodeng003')
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'deleted'
