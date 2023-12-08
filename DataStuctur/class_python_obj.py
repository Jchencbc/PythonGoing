import math
"""
编写一个典型的python对象
__x和__y双下划线开头属性为私有属性

"""

class Vector:
    typecode = 'd'
    # __slots__ = ('__x', '__y')
    def __init__(self, x:float, y:float) -> None:
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
        return  '{}({!r}, {!r})'.format(cls_name, *self)

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
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

class myVector(Vector):
    typecode = 'f'

