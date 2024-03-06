#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:6/3/2024 下午 2:26
"""
import numbers

"""
简易版django的orm实现
"""


class Field:
    ...


class CharField(Field):
    def __init__(self, db_name, max_length=None):
        self._value = None
        self.db_name = db_name
        if max_length:
            self.max_length = max_length
        else:
            raise ValueError('max_length is not None')
        if not isinstance(self.max_length, numbers.Integral):
            raise ValueError('max_length is not pastive int')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if len(value) > self.max_length:
            raise ValueError('value length excess len of max_length')
        self._value = value


class MetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fileds = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                fileds[k] = v
        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_name", None)
            if table is not None:
                db_table = table
        _meta['db_table'] = db_table
        attrs["_meta"] = _meta
        attrs["field"] = fileds
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=MetaClass):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        super().__init__()  # 这个的作用？

    def save(self):
        print('ssssss')


class User(BaseModel):
    name = CharField(db_name='Name', max_length=10)  # 属性描述符

    class Meta:
        db_name = 'user'


if __name__ == "__main__":
    user = User(name='jinchen')
    user.save()
