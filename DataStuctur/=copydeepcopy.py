"""
python 中的= 浅拷贝 和 深拷贝
"""

import copy


a = [1, 2, 3, [1, 2]]
b = a  # 赋值，其实就是对象的引用（别名）
c = a.copy()  # 浅拷贝 拷贝父对象，不会拷贝对象的内部的子对象。
d = copy.deepcopy(a)  # 深拷贝 拷贝父对象，拷贝对象的内部的子对象。

b.append(99)
print(a)
c.append(100)
print(a)
c[3].append(100)
print(a)
d.append(101)
print(a)
