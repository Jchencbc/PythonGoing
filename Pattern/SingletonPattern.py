"""
单例模式：单例的类只实例化一次。它常常应用于数据库操作、日志函数。
"""

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):  # new方法构建单例模式
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self) -> None:
        pass

a = Singleton()
b = Singleton()
print(id(a), id(b))
# 复写内部方法__new__()
# 通过hasattr函数判断该类实例化时有没有_instance属性
# 如果不存在，那么继承并返回原始的__new__方法给_instance属性
# 如果存在则直接返回_instance属性所指的对象