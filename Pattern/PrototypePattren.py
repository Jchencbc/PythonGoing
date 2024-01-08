
"""
原型模式：拷贝、属性更新.原型模式的想法是使用该对象的完整结构的拷贝来产生新的对象
"""
import copy
class Car:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size
    
    def __str__(self) -> str:
        return 'my car is {}, {}, {}'.format(self.name, self.color, self.size)

class Ptototype:
    def __init__(self) -> None:
        self._clone_objects = {}
    
    def register_object(self, name, obj):
        self._clone_objects[name] = obj
    
    def del_register_object(self, name):
        del self._clone_objects[name]
    
    def clone_obj(self, name, **kwargs):  # 实现copy方法，快速复制模板对象
        obj = copy.deepcopy(self._clone_objects[name])
        obj.__dict__.update(**kwargs)  # 对模板对象自定义
        return obj
    
if __name__ == '__main__':
    pass