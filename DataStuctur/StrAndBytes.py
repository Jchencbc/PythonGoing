#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:30/11/2023 上午 9:22
"""

"""
文本总是Unicode，由str类型表示
二进制数据则由bytes类型表示
Unicode编码：把所有语言都统一到一套编码里，用两个字节表示一个字符
UTF-8编码：把Unicode编码转化为“可变长编码”，UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

码位：字符的标识.Unicode
字节：字符的具体表述取决于所用的编码.默认utf-8
"""
import sys, locale

if __name__ == "__main__":
    a = 'sss我'
    b = a.encode('utf-8')
    print(b)

    expressions = """
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
    """
    my_file = open('dummy.txt', 'w')
    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', repr(value))
