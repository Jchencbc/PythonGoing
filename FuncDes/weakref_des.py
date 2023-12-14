"""
介绍python弱引用机制
"""
import threading
import weakref

class Data:
    def __init__(self, key):
        pass

# 数据缓存
class Cacher:
    def __init__(self):
        self.pool = {}
        self.lock = threading.Lock()
    def get(self, key):
        with self.lock:
            if data:
                return data
            data = Data(key)
            self.pool[key] = data  # 弱引用改造
            return data

class CacherTwo:
    def __init__(self):
        self.pool = {}
        self.lock = threading.Lock()
    def get(self, key):
        with self.lock:
            r = self.pool.get(key)
            if r:
                data = r()
                if data:
                    return data
            data = Data(key)
            self.pool[key] =weakref.ref(data)  # 弱引用改造
            return data

"""
存在内存泄漏的风险， Data 一旦被创建后，就保存在缓存字典中，永远都不会释放
解决方案：弱引用 ->弱引用是一种特殊的对象，能够在不产生引用的前提下，关联目标对象
"""
d = Data('my_data')
ref_d = weakref.ref(d)  # 创建一个引向该对象的若引用
print(ref_d())
print(ref_d() is d)
del d  # 清楚引用标记，释放内存
print(ref_d())  # 弱引用也被清空


"""
weakref.WeakKeyDictionary     键只保存弱引用的映射类
weakref.WeakValueDictionary   值只保存弱引用的映射类
"""
# 数据缓存
class CacherThree:
    def __init__(self):
        self.pool = weakref.WeakValueDictionary()
        self.lock = threading.Lock()
    def get(self, key):
        with self.lock:
            data = self.pool.get(key)
            if data:
                return data
            self.pool[key] = data = Data(key)
            return data

