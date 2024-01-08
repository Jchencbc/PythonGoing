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

# charfinder.py
import sys
import re
import unicodedata
import pickle
import warnings
import itertools
import functools
from collections import namedtuple

# tcp_charfinder.py
import sys
import asyncio

# 用于构建索引，提供查询方法
from charfinder import UnicodeNameIndex

CRLF = b'\r\n'
PROMPT = b'?> '

# 实例化UnicodeNameIndex 类，它会使用charfinder_index.pickle 文件
index = UnicodeNameIndex()

async def handle_queries(reader, writer):
    # 这个协程要传给asyncio.start_server 函数，接收的两个参数是asyncio.StreamReader 对象和 asyncio.StreamWriter 对象
    while True:  # 这个循环处理会话，直到从客户端收到控制字符后退出
        writer.write(PROMPT)  # can't await!  # 这个方法不是协程，只是普通函数；这一行发送 ?> 提示符
        await writer.drain()  # must await!  # 这个方法刷新writer 缓冲；因为它是协程，所以要用 await
        data = await reader.readline()  # 这个方法也是协程，返回一个bytes对象，也要用await
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            # Telenet 客户端发送控制字符时，可能会抛出UnicodeDecodeError异常
            # 我们这里默认发送空字符
            query = '\x00'
        client = writer.get_extra_info('peername')  # 返回套接字连接的远程地址
        print('Received from {}: {!r}'.format(client, query))  # 在控制台打印查询记录
        if query:
            if ord(query[:1]) < 32:  # 如果收到控制字符或者空字符，退出循环
                break
            # 返回一个生成器，产出包含Unicode 码位、真正的字符和字符名称的字符串
            lines = list(index.find_description_strs(query)) 
            if lines:
                # 使用默认的UTF-8 编码把lines    转换成bytes 对象，并在每一行末添加回车符合换行符
                # 参数列表是一个生成器
                writer.writelines(line.encode() + CRLF for line in lines) 
            writer.write(index.status(query, len(lines)).encode() + CRLF) # 输出状态

            await writer.drain()  # 刷新输出缓冲
            print('Sent {} results'.format(len(lines)))  # 在服务器控制台记录响应

    print('Close the client socket')  #  



def main(address='192.168.31.132', port=2323):  # 添加默认地址和端口，所以调用默认可以不加参数
    port = int(port)
    loop = asyncio.get_event_loop()
    # asyncio.start_server 协程运行结束后，
    # 返回的协程对象返回一个asyncio.Server 实例，即一个TCP套接字服务器
    server_coro = asyncio.start_server(handle_queries, address, port) 
    server = loop.run_until_complete(server_coro) # 驱动server_coro 协程，启动服务器

    host = server.sockets[0].getsockname()  # 获得这个服务器的第一个套接字的地址和端口
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))  # 在控制台中显示地址和端口
    try:
        loop.run_forever()  # 运行事件循环 main 函数在这里阻塞，直到服务器的控制台中按CTRL-C 键
    except KeyboardInterrupt:  # CTRL+C pressed
        pass

    print('Server shutting down.')
    server.close()
    # server.wait_closed返回一个 future
    # 调用loop.run_until_complete 方法，运行 future
    loop.run_until_complete(server.wait_closed())  
    loop.close()  # 终止事件循环


if __name__ == '__main__':
    main(*sys.argv[1:])