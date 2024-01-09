"""
外观模式： 为子系统中的一组接口提供一个一致的界面，Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

与接口相关的适配器模式有所不同的是外观模式是为大系统下的小系统设计统一的接口，而适配器模式是针对不同系统各种接口调用而设计。
"""

class API1:

    def Save(self):
        print('保存数据A')

    def Del(self):
        print('删除数据A')


class API2:

    def Save(self):
        print('保存数据B')

    def Del(self):
        print('删除数据B')


class Facade:

    def __init__(self):
        self._api1 = API1()
        self._api2 = API2()

    def SaveAll(self):
        [obj.Save() for obj in [self._api1, self._api2]]

    def DelAll(self):
        [obj.Save() for obj in [self._api1, self._api2]]


if __name__ == '__main__':
    test = Facade()
    test.SaveAll()
    test.DelAll()