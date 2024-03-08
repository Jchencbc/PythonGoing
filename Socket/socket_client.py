#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:7/3/2024 下午 4:01
"""
"""
socket 服务端
"""
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    re_data = input()
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))
