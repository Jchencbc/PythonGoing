#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:7/3/2024 下午 4:00
"""
import threading
import socket

"""
socket 用户端
"""


def handle_sock(client_sock, client_addr):
    while True:  # 死循环监听客户端
        data = client_sock.recv(1024)  # 限定访问字节
        print(data.decode('utf8'))
        re_data = input()  # 输入返回
        client_sock.send(re_data.encode('utf8'))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 绑定8000端口
server.listen()
while True:  # 死循环监听客户端
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))  # 开启多线程监听多个客服端
    client_thread.start()
