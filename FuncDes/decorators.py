#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   decorators.py
@Time    :   2023/12/06 10:32:54
@Author  :   jinChen 
@Version :   1.0
@Email   :   278229887@qq.com
'''

"""
装饰器和闭包
"""
import functools
import time


def make_average():
    count = 0
    total = 0
    
    def averager(value):
        nonlocal count,total  # 自由变量nonlocal声明,对于不可修改的元素，要在闭包内修改需要用自由变量声明
        count +=1
        total += value
        return total / count

    return averager

test = make_average()
print(test(1))
print(test(2))
print(test(3))

def clock(func):
    def clocked(*args):  
        t0 = time.perf_counter()
        result = func(*args)  
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked #

@functools.lru_cache()  # 缓存装饰器
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result 
        return clocked 
    return decorate



if __name__ == "__main__":
    @clock()
    def snooze(seconds):
        time.sleep(seconds)
        
    for i in range(3):
        snooze(1)