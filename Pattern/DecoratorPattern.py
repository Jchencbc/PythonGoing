"""
装饰模式:装饰模式指的是在不必改变原类文件和使用继承的情况下，动态地扩展一个对象的功能。它是通过创建一个包装对象，也就是装饰来包裹真实的对象。
"""
class Test:
    def add(self):
        print("增加数据")
    def remove(self):
        print('删除数据')
class Decorator:
    def __init__(self,name):
        self._run = name
    def save(self):
        print("保存数据")
    def __getattr__(self, item):
        return getattr(self._run, item)
if __name__ == '__main__':
    t1 = Test()
    t2 = Decorator(t1)
    t2.remove()
    t2.add()
    t2.save()
    
"""
1. 多组合，少继承。

利用继承设计子类的行为，是在编译时静态决定的，而且所有的子类都会继承到相同的行为。然而，如果能够利用组合的做法扩展对象的行为，就可以在运行时动态地进行扩展。

2. 类应设计的对扩展开放，对修改关闭。
"""