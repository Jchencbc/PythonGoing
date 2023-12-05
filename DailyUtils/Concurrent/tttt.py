#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
data:10/11/2023 下午 5:15
"""
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("sss")
        return func(*args, **kwargs)
    return wrapper


@decorator
def my_test(x, y):
    print('lalala')


my_test(3, 4)

