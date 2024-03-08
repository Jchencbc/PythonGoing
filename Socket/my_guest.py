#!/usr/bin/env python3
# coding=utf-8

from socket import *
from threading import Thread


class TcpClient(object):
    """Tcp客户端"""

    def __init__(self, IP="127.0.0.1", Port=8888):
        """初始化对象"""
        self.code_mode = "utf-8"  # 收发数据编码/解码格式
        self.IP = IP
        self.Port = Port
        self.my_socket = socket(AF_INET, SOCK_STREAM)  # 创建socket

    def run(self):
        """启动"""
        self.my_socket.connect((self.IP, self.Port))  # 连接服务器

        tr = Thread(target=self.recv_data)  # 创建线程收数据
        ts = Thread(target=self.send_data)  # 创建线程发数据

        tr.start()  # 开启线程
        ts.start()

    def recv_data(self):
        """收数据"""
        while True:
            data = self.my_socket.recv(1024).decode(self.code_mode)
            if data:
                print("\r>>{}\n<<".format(data), end="")
            else:
                break

        self.my_socket.close()

    def send_data(self):
        """发数据"""
        while True:
            data = input(">>")
            self.my_socket.send(data.encode(self.code_mode))


def main():
    print("\033c", end="")  # 清屏
    ip = input("请输入服务器IP:")
    port = int(input("请输入服务器Port:"))
    my_socket = TcpClient(ip, port)
    my_socket.run()


if __name__ == "__main__":
    main()
