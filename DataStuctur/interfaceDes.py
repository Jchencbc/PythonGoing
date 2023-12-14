"""
python接口 协议 抽象基类
"""

from collections import abc
import random
from typing import Any

class Stuggel:
    def __len__(self):
        return 3

a = Stuggel()

print(isinstance(a, abc.Sized))  # 无需注册 只要实现了__len__方法 abc.Sizes

import abc

class School(abc.ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加学生"""
    
    @abc.abstractmethod
    def pick(self):
        """删除一位学生返回"""
    
    def getData(self):
        """返回当前学生信息"""
        items = []
        while True:
            try:
                items.append(self.pick()) 
            except LookupError:  # 抛出异常
                break
        self.load(items)
        return tuple(items)

class MiddleSchool(School):
    
    def __init__(self, students) -> None:
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(students)
    
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.pick()




"""
虚拟子类和register机制
虚拟子类是将其他的不是从抽象基类派生的类”注册“到抽象基类，让Python解释器将该类作为抽象基类的子类使用，因此称为虚拟子类，
这样第三方类不需要直接继承自抽象基类。注册的虚拟子类不论是否实现抽象基类中的抽象内容，Python都认为它是抽象基类的子类，调用 issubclass(子类，抽象基类),isinstance (子类对象，抽象基类)都会返回True。
当一个类继承自抽象基类时，该类必须完成抽象基类定义的语义；当一个类注册为虚拟子类时，这种限制则不再有约束力，可以由程序开发人员自己约束自己，因此提供了更好的灵活性与扩展性
"""

@School.register  # 注册
class Kindergarden():
     def __init__(self,students):self.students=list(students)
     def showNumber(self):return len(self.students)

boshiwa=Kindergarden(['aa','bb'])
issubclass(Kindergarden,School)
isinstance(boshiwa,School)