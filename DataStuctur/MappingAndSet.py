#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:29/11/2023 上午 10:05
"""
# 可变字典&不可变字典
import collections
from collections import abc
from types import MappingProxyType

"""
Container.Iterable.Sized
Mapping:__getitem__,__contains__,__eq__,__ne__,get,items,keys,values  不可变
MutableMapping:__setitem__,__delitem__,clear,pop,popitem,setdefault,update  可变
"""

# 标准库中映射类型都是用dict实现的，只有可散列（可哈希）的数据类型能作为key
"""
（1）支持 hash() 函数，并且通过__hash__()方法得到的散列值是不变的
（2）支持通过__eq__()方法检测相等性
（3）若a==b为真，则hash(a)==hash(b)也为真
"""

if __name__ == "__main__":
    a = {}
    print(isinstance(a, abc.Mapping))  # abc抽象基类
    print(isinstance(a, abc.MutableMapping))

    a = dict(one=1, two=2)
    a = dict([('one', 1), ('two', 2)])
    a = dict({'one': 1, 'two': 2})
    DIAL_CODES = [([86], 'China'), ([91], 'India'), ([1], 'United States'), ([62], 'Indonesia')]
    a = {country: code for code, country in DIAL_CODES}  # 字典推导式

    # setdefault用法。字典找不到值是设置默认值，规避get的复杂操作
    test = 10000
    tmp = a.get('Jin', [])
    tmp.append(test)
    a['Jin'] = tmp
    a.setdefault('Jin', []).append(test)
    print(a)

    # defaultdict：处理找不到键的选择. 重写__missing__方法
    b = collections.defaultdict(list)
    b['Jin'].append('10000')
    b['Jin'].append('20000')
    print(b)


    # 自定义字典，UserDict.重写__missing__方法、get方法、__contains__方法
    class MyDict(collections.UserDict):
        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self.data[str(key)]

        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default

        def __contains__(self, key):
            return key in self.data or str(key) in self.data

        def __setitem__(self, key, value):
            self.data[str(key)] = value


    a = MyDict({'2': 'two', '3': 'three'})
    print(3 in a)  # 不建议，建议使用key in a.keys() 后者返回为视图，效率会更快
    print(type(a.keys()))  # <class 'collections.abc.KeysView'>
    print(a[3], a['3'])
    a[4] = 'four'
    print(a['4'], a[4])

    # OrderDict 添加键的时候会保持顺序.popitem 方法默认删除并返回的是字典里的最后一个元素
    a = collections.OrderedDict({'2': 'two', '3': 'three', '4': 'three'})
    a.popitem()
    a.popitem()
    print(a)

    # ChainMap 修改时，只会对第一个字典修改
    a = collections.ChainMap({'2': 'two', '3': 'three'}, {'4': 'four'})
    print(a.get('4'))

    # Counter
    ct = collections.Counter('abracadabra')
    print(ct)
    ct.update('aaaaazzz')
    ct.most_common(2)

    # 不可变映射类型
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)  # MappingProxyType 来获取字典的只读实例mappingproxy\
    print(type(d_proxy), d_proxy)  # <class 'mappingproxy'> || {1: 'A'}
    # d_proxy[2] = 'C'  # 报错映射字典无法修改
    d[2] = 'c'  # 通过修改原字典，来修改映射字典
    print(d_proxy)

    """
    集合set&frozenset:集合中的元素必须是可散列的，set不可散列，frozenset可散列
    Container.Iterable.Sized
    Set:__le__,__lt__,__gt__,__ge__,__eq__,__ne__,__and__,__or__,__sub__,__xor__  不可变
    MutableSet:add,discard,remove,pop,clear,__ior__,__iand__,__ixor__,__isub__  可变
    """
    a = {'2', '3'}
    b = {'2', '4'}
    print(a | b)
    print(a & b)
    print(a - b)  # 和、交、差
    a = frozenset(range(10))

    """
    字典和集合的背后（散列表）
    散列表其实是一个稀疏数组（总是有空白元素的数组称为稀疏数组）
    散列表里的单元通常叫作表元（bucket）
    dict 的散列表当中，每个键值对都占用一个表元，每个表元都有两个部分，一个是对键的引用，另一个是对值的引用。因为所有表元的大小一致，所以可以通过偏移量来读取某个表元。
    Python 会设法保证大概还有三分之一的表元是空的，所以在快要达到这个阈值的时候，原有的散列表会被复制到一个更大的空间里面。
    要把一个对象放入散列表，那么首先要计算这个元素键的散列值。Python 中可以用 hash() 方法来做这件事情. __hash__  __eq__
    散列表算法
    """
