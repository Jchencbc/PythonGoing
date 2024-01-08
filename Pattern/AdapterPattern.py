"""
适配器模式，他的实现是以我们定义的适配器函数来分类，将各种类的不同方法注册到对应的分类函数中，调用的时候只需要使用分类名，这样就达到了适配所有类不同方法的效果.
"""
class Computer:
    def __init__(self) -> None:
        pass
    
    def execute(self):
        pass

class PhotoScreen:
    def __init__(self) -> None:
        pass
    
    def photo(self):
        pass

class Television:
    def __init__(self) -> None:
        pass
    
    def play(self):
        pass

class Adapter:
    def __init__(self, obj, adapted_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)  # 实现适配器

if __name__ == '__main__':
    """
    采用适配器后，所有类都是用execute()启动
    """
    objects=[Computer()]
    synth=Television()
    objects.append(Adapter(synth,dict(execute=synth.play)))
    human=PhotoScreen()
    objects.append(Adapter(human,dict(execute=human.photo)))
    for i in objects:
        print('{} {}'.format(str(i),i.execute()))