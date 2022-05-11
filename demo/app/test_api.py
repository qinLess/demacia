# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: test_api.py
    Time: 2021/7/14 下午5:06
-------------------------------------------------
    Change Activity: 2021/7/14 下午5:06
-------------------------------------------------
    Desc: 
"""
import requests


def test_js_client_time():
    url = 'http://127.0.0.1:10521/demaica/asyncInvoke'

    data = {
        'group_id': 'ws_group',
        'action_name': 'clientTime'
    }

    res = requests.post(url, json=data)

    print('clientTime: ', res.text)


def test_hello_world():
    url = 'http://127.0.0.1:10521/demaica/asyncInvoke'

    data = {
        'group_id': 'ws_group',
        'action_name': 'get_hello_world',
        'params': {
            'a': 'aaa',
            'b': 'bbb',
        }
    }

    res = requests.post(url, json=data)

    print('test_hello_world: ', res.text)


def get_x_sign_8110():
    url = 'http://127.0.0.1:10521/demaica/asyncInvoke'

    params = {
        "v": "8110",
        "input": "&&&23181017&1ba1770e41fdd4cb3335ff0576a0aa3b&1626252190&mtop.tmall.inshopsearch.searchitems&1.0&&231200@tmall_android_8.11.0&AnlJxyMxqq1WP7ZOSURHlmKQRVnNJ8Y7la4LNiuKMrpD&&&27&&&&&&&",
        "app_key": "23181017"
    }

    data = {
        'group_id': 'tianmao',
        'action_name': 'get_x_sign_8110',
        'params': params
    }

    res = requests.post(url, json=data)

    print('get_x_sign_8110: ', res.text)


if __name__ == '__main__':
    get_x_sign_8110()

    # test_hello_world()
    # test_js_client_time()
