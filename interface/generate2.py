#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:generate2.py
@time:2020/11/30
"""
import json

from mitmproxy import http


def respose(flow: http.HTTPFlow):
    url = flow.request.url.split('.json')[0]
    if 'quote.json' in flow.request.url:
        date = json.loads(flow.response.content)
        # 修改

        data_new = json.dumps(date)
        flow.response.text = json.dumps(data_new)


def json_increase(data, array=None, num=None, text=None):
    '''
    :param data:
    :param array:
    :param num:
    :param text:
    :return: data_new
    example：
            {
              "name": "chenshifeng",
              "age": 18,
              "interest": ["song","eat","TV","movie"],
              "work": {
                "company1": "software testing",
                "company2": " software development"
              }
            }
    '''
    data_new = None
    if isinstance(data, dict):
        data_new = dict()
        for k, v in data.items():
            data_new[k] = json_increase(v, array, num, text)

    elif isinstance(data, list):
        data_new = list()
        for item in data:
            new_item = json_increase(item, array, num, text)
            if array is None:
                data_new.append(new_item)
            else:
                if isinstance(array, int) and array > 0:
                    for i in range(array):
                        data_new.append(new_item)
                else:
                    # data_new.append(new_item)
                    data_new = data

    elif isinstance(data, str):
        if isinstance(text, int) and text > 0:
            data_new = data * text
        else:
            data_new = data

    elif isinstance(data, int) or isinstance(data, float):
        if data is not True:
            data_new = data * num
            # return data_new

    else:
        data_new = data

    return data_new


if __name__ == '__main__':
    data = {
        "name": "chenshifeng",
        "age": 18,
        "interest": ["song", "eat", "TV", "movie"],
        "work": {
            "company1": "software testing",
            "company2": " software development"
        }
    }
    print(json_increase(data, num=2))
