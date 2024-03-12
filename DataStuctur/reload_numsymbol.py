"""
python关于重载运算符的规定:
不能重载内置类型的运算符
不能新建运算符，只能重载现有的
某些运算符不能重载——is、and、or 和 not（不过位运算符&、| 和 ~ 可以）
"""

"""
一元运算符
-（__neg__）  一元取负算术运算符。
+（__pos__）  一元取正算术运算符
~（__invert__）  对整数按位取反
"""

import itertools
import math
from DataStuctur.class_python_obj import Vector


class Vector3(Vector):
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector3(-x for x in self)

    def __pos__(self):
        return Vector3(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):  # 右向加法
        return self + other
