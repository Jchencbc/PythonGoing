#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
网络编程socket
多线程的网络通讯python实现
"""

"""
同步框架
异步框架
"""


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]

    start_response(status, headers)
    return [b"<h1>Hello</h1>"]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()
