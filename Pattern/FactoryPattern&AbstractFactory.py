"""
抽象工厂：创建一系列相关或相互依赖抽象出来的的对象接口Interface，不需要具体指明实例化A类或B类

工厂方法：定义一个用于创建对象的接口函数Interface，让子类决定实例化哪一个类A或者B
"""


class SchoolTypeOne():
    def __init__(self, name:str, number:int) -> None:
        self.name = name
        self.number = number
        
    def say(self):
        print('my name is {}'.format(self.name))
    
    def count(self):
        print('my number is {}'.format(self.number))

class SchoolTypeTwo():
    def __init__(self, name:str, number:int) -> None:
        self.name = name
        self.number = number
        
    def say(self):
        print('my name is {}'.format(self.name))
    
    def count(self):
        print('my number is {}'.format(self.number))

def SchoolInterface(school_name, name, count):  # 工厂模式，将同质的类集合在一起，抽象封装成一个类函数
    school_dict = {'school_one':SchoolTypeOne, 'school_two':SchoolTypeTwo}
    return school_dict[school_name](name, count)  # 返回类

school_one = SchoolInterface('school_one', 'xiaoxue', 33)
school_two = SchoolInterface('school_two', 'youeryuan', 44)
school_one.say()


class SchoolInterface():
    
    def __init__(self, schoole_name, name, count) -> None:
        self.school = schoole_name(name, count)
    
    def say(self):
        return self.school.say()
    
    def count(self):
        return self.school.count()