#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:1/12/2023 上午 9:38
"""

if __name__ == "__main__":
    print(dir(dict))  # dir


    class MyType:

        def __init__(self, value: int):
            self.value = value

        def pick(self) -> int:
            if self.value > 0:
                return self.value - 1
            return -1

        def __call__(self, *args, **kwargs):  # 实现了__call__方法 类实例化对象可以直接调用；callable()判断对象是否可调用
            return str(self.pick()) + '调用call'


    test_cls = MyType(5)
    print(test_cls())
    print(callable(test_cls))


    def myfunc(a, b=2, *args, c=10, **kwargs) -> int:  # 函数位置参数和关键字参数
        """
        用于测试
        :return: None
        """
        if args:
            for i in args:
                print("{},{},{},位置参数{}".format(a, b, c, i))
        else:
            print("{},{},{}".format(a, b, c))
        if kwargs:
            for _, v in kwargs.items():
                print("{},{},{},关键字参数{}".format(a, b, c, v))
        else:
            print("{},{},{}".format(a, b, c))
        return 1


    # a = myfunc(1, 2, c=1, d=2)
    b = myfunc(1, 2, 3, 4, c=16, d=2, e=5)

    print(myfunc.__defaults__)  # 参数默认值
    print(myfunc.__kwdefaults__)  # 仅限关键字参数默认值

    print("*"*20)
    print(myfunc.__code__)
    print(myfunc.__code__.co_varnames)  # 函数变量
    print(myfunc.__code__.co_argcount)  # 确定参数名数量

    # inspect模块


