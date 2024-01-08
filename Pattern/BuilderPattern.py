"""
建造者模式：建造者模式（Builder Pattern）是一种创建型设计模式，它用于构建一个复杂对象的各个部分，并允许按步骤构造。这种模式下，同样的构建过程可以创建不同的表示（representation）。
"""
class Director:  # 建造指挥者类
    _builder = None  # 指定特定建造者
    
    def set_builder(self, builder):
        self._builder = builder
    
    def get_cat(self):  # 建造流程
        my_car = Car()
        my_car.set_body(self._builder.get_body())
        my_car.set_engine(self._builder.get_engine())
        i = 0 
        while i<4:
            my_car.set_wheel(self._builder.get_wheel())
            i+=1
        return my_car
    
class Car():  # 产品类抽象
    def __init__(self) -> None:
        self.__wheels = []
        self.__engine = None
        self.__body = None
    
    def set_body(self, body):
        self.__body = body
    
    def set_engine(self, engine):
        self.__engine = engine
    
    def set_wheel(self, wheel):
        self.__wheels.append(wheel)
    
    def specification(self):
        print("body is {} engine is {} wheels is {}".format(self.__body, self.__engine, ''.join(self.__wheels)))

class Builder():  # 建造基类
    def get_wheel(self):pass
    def get_engine(self):pass
    def get_body(self):pass

class BenCiCar(Builder):  # 特定建造者实现不同建造内容
    def get_wheel(self):
        return '300'
    def get_engine(self):
        return 10000
    def get_body(self):
        return 'suv'

if __name__=='__main__':
    benci_bulider = BenCiCar()
    director = Director()
    director.set_builder(benci_bulider)
    benci_car = director.get_cat()
    benci_car.specification()