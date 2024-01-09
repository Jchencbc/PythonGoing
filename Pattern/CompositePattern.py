"""
组合模式：组合，将对象组合成树状结构，来表示业务逻辑上的[部分-整体]层次，这种组合使单个对象和组合对象的使用方法一样。
"""
import abc


class ComponentBases(abc.ABC):
    def __init__(self, name, duty) -> None:
        self.name = name
        self.duty = duty
        self.children = []
    
    @abc.abstractclassmethod
    def add(self):
        pass
    
    @abc.abstractclassmethod
    def remove(self):
        pass
    
    @abc.abstractclassmethod
    def display(self):
        pass

class CompanyNode(ComponentBases):
    def __init__(self, name, duty) -> None:
        super().__init__(name, duty)
    
    def add(self, obj):
        self.children.append(obj)

    def remove(self, obj):
        self.children.remove(obj)

    def display(self, number=1):
        print("部门：{} 级别：{} 职责：{}".format(self.name, number, self.duty))
        n = number+1
        for obj in self.children:
            obj.display(n)

if __name__ == '__main__':
    root = CompanyNode("总经理办公室", "总负责人")
    node1 = CompanyNode("财务部门", "公司财务管理")
    root.add(node1)
    node2 = CompanyNode("业务部门", "销售产品")
    root.add(node2)
    node3 = CompanyNode("生产部门", "生产产品")
    root.add(node3)
    node4 = CompanyNode("销售事业一部门", "A产品销售")
    node2.add(node4)
    node5 = CompanyNode("销售事业二部门", "B产品销售")
    node2.add(node5)
    root.display()