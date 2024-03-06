#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:6/3/2024 下午 1:29
"""
from collections.abc import Iterable


class User:
    def __new__(cls, *args, **kwargs):
        print('new方法，用于构造实例，控制类的实例化过程')
        return super().__new__(cls)  # 返回，否则将不会执行__init__

    def __init__(self):
        print('init方法，实例属性初始化')


class MetaClassDes(type):
    """
    继承type 控制类的生成
    """
    def __new__(cls, *args, **kwargs):
        print('xxx')
        return super().__new__(cls, *args, **kwargs)


class MetaclassUser(metaclass=MetaClassDes):
    """
    metaclass控制类的生成
    """
    name = 'test'

    def __str__(self):
        return self.name


if __name__ == "__main__":
    # a = type('Type_User', (), {})  # type创建类
    # print(a)

    c = MetaclassUser()
    print(c)
