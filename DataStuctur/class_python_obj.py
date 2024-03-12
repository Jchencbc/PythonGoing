import array
import functools
import itertools
import math
import operator
import reprlib

"""
编写一个典型的python对象
__x和__y双下划线开头属性为私有属性

"""


class Vector:
    typecode = 'd'

    # __slots__ = ('__x', '__y')
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self) -> str:
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        return '{}({!r}, {!r})'.format(cls_name, *self)

    def __str__(self) -> str:
        return str(tuple(self))

    def __eq__(self, __value: object) -> bool:
        return tuple(self) == tuple(__value)

    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __boo__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, __format_spec: str) -> str:
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):  # 类方法常见用途，定义备选构造方法
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


class VectorV2:
    typecode = 'd'

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, __value: object) -> bool:
        return len(self) == len(object) and all(a == b for a, b in zip(self, __value))

    def __hash__(self) -> int:
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, int):
            return self._components[index]
        else:
            msg = '{.__name__} indices must be integers'
            raise TypeError(msg.format(cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.endswith('h'):
            __format_spec = __format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, __format_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


class TestMonkeyPatch:
    say = 'sssss'


def eaqual_path(a, b) -> bool:
    return len(a.say) == len(b)


TestMonkeyPatch.__eq__ = eaqual_path  # 猴子补丁运行时实现__eq__.在运行时修改类或模块，而不改动源码

mytest = TestMonkeyPatch()
print(mytest == 'ssssqss')
