# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: frida_hook.py
    Time: 2021/7/31 下午2:37
-------------------------------------------------
    Change Activity: 2021/7/31 下午2:37
-------------------------------------------------
    Desc: 
"""
import os

import frida

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script.js')
apk_info = {
    'process_list': [],
    'app_name': '天猫',
    'script_path': script_path,
    'apk_package_name': 'com.tmall.wireless',
    'apk_main_activity': 'com.tmall.wireless/.splash.TMSplashActivity'
}


def get_device():
    try:
        # 此脚本如果在电脑需要使用这个 函数获取 设备
        device = frida.get_device('73fe1d8a')
        # 如果脚本在手机上 使用此函数即可
        # device = frida.get_local_device()
        return device

    except Exception as e:
        print(f'get_devices.error: {e}')


def get_device_instance():
    devices = get_device()
    print(f'attach {apk_info["app_name"]}: {devices}')

    with open(f'{apk_info["script_path"]}', 'r', encoding='utf-8') as f:
        js_code = f.read()

    process_pid = devices.attach(apk_info['apk_package_name'])
    script = process_pid.create_script(js_code)
    script.load()
    return script


device_instance = get_device_instance()


def get_x_sign_8110(params):
    try:
        return device_instance.exports.getxsign8110(params)

    except Exception as e:
        print(f'get_x_sign_8110.e: {e}')

        return str(e)


def get_mini_wua_8110(params):
    try:
        return device_instance.exports.getminiwua8110(params)

    except Exception as e:
        print(f'get_mini_wua_8110.e: {e}')

        return str(e)
