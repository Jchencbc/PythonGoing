#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:6/3/2024 上午 11:09
"""
import datetime

"""
主要介绍python的属性相关
"""


class PropertyDes:
    def __init__(self, name):
        self.name = name
        self._age = None

    @property  # get时候加入逻辑
    def age(self):
        return datetime.date.today().year

    @age.setter  # settter时候加入逻辑
    def age(self, value):
        self._age = value

    def __getattr__(self, item):
        """
        查找属性没有找到时候调用
        """
        return 'not found'

    # def __getattribute__(self, item):
    #     """
    #     优先级最高，在getattr和属性查找之前。不要轻易写
    #     """
    #     return 'xxxxx'


class StringField:
    """
    定义一个属性描述符,
    必须实现get,set,delete方法
    """

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("value is not Sring type")
        self.value = value  # 属性描述符的复制

    def __delete__(self, instance):
        pass


class NonDataDescriptor:
    """
    定义一个非数据属性描述符,
    必须实现get方法
    """

    def __get__(self, instance, owner):
        return "这是一个非数据的属性描述符"


class User:
    age = 1  # __dict__['age']
    name = StringField()  # 属性描述符号
    non_data = NonDataDescriptor()  # 非数据属性描述符

    def __init__(self, info, name):
        self.info = info  # obg.__dict__['info']
        self.name = name


"""
user是User的实例。 user.age调用：
__getattribute__ 首先调用，如果类定义了__getattr__方法，那么在__getattribute__ 抛出AttributeError时调用__getattr__
描述符__get__调用发生在__getattribute__内部
user.age:
1:age在User或其基类__dict__中， 且age是 data descriptor 调用__get__方法，否则
2:age在user的__dict__中，直接返回obg.__dict__['age']，否则
3:"age"出现在User或其基类__dict__中
  3.1：如果age是non-data descriptor，则调用其__get__方法，否则
  3.2：返回__dict__['age']
4:如果User有__getattr__方法，调用该方法。 否则抛出AttributeError
"""

if __name__ == "__main__":
    # 动态属性
    test_one = PropertyDes("aaa")
    test_one.age = 30  # 调用setter
    print(test_one.age)  # 调用get
    print(test_one._age)

    print(test_one.gender)  # 调用getattr

    test_two = User(info='info_cls', name='1')
    print(test_two.__dict__)
    print(User.__dict__)
    print(test_two.name)  # 看下这个逻辑
