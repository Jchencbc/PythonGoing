#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:12/3/2024 下午 2:07
"""

"""
链表
"""


class Node:
    def __init__(self, value=None, next=None):
        self._value = value  # 数据
        self._next = next  # 指向下个节点

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, new_value):
        self._value = new_value

    def setNext(self, new_next):
        self._next = new_next


class LinkedList:
    def __init__(self):
        self._head = None  # 初始化
        self._tail = None
        # self._length = 0

    def isEmpty(self):
        return self._head is None

    def add(self, value):
        """链表前端添加元素"""
        node = Node()
        node.setValue(value)
        node.setNext(self._head)
        self._head = node
        # self._length += 1

    def append(self, value):
        """尾部添加元素"""
        node = Node()
        node.setValue(value)
        if self.isEmpty():
            self._head = node  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() is not None:
                current = current.getNext()  # 遍历链表
            current.setNext(node)  # 此时current为链表最后的元素

    def search(self, value):
        """查找元素"""
        current = self._head
        while current is not None:
            if current.getValue() == value:
                return True
            current = current.getNext()
        return False

    def index(self, value):
        """查找元素返回下标"""
        current = self._head
        if not self.search(value):
            return 'Error'
        index = 1
        while current is not None:
            if current.getValue() == value:
                return index
            index += 1
            current = current.getNext()

    def remove(self, value):
        """删除元素"""
        ...

    def __len__(self):
        i = 0
        current = self._head
        while current is not None:  # 非空
            i += 1
            current = current.getNext()
        return i

    def insert(self, value, index):
        """插入元素"""
        i = 1
        current = self._head
        if index < 1 or index > len(self) + 1:
            return 'Error'  # 超出链表插入位置
        if index == 1:
            node = Node(value, current)
            self._head = node
            return 'ok'
        while i < index - 1:  # 插入位置前的元素
            current = current.getNext()
            i += 1
        node = Node(value, current.getNext())
        current.setNext(node)
        return 'ok'


if __name__ == "__main__":
    ...
