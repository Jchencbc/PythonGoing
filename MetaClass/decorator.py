#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
data:13/11/2023 上午 9:19
"""
import logging
import time
import types

from functools import wraps, partial

from inspect import signature
from functools import wraps


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


if __name__ == "__main__":
    # As an instance method
    @Profiled
    def add(x, y):
        return x + y


    class Spam:
        @Profiled
        def bar(self, x):
            print(self, x)


    # add(2, 3)
    # print(add.ncalls)
    s = Spam()
    s.bar(3)
