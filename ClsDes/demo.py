import copy


class BusMoving:
    
    def __init__(self, passangers) -> None:
        if passangers is None:
            self.passangers = []
        else:
            # self.passangers = passangers  # 直接赋值，修改原数据
            # self.passangers = copy.copy(passangers)  # 可变类型，为了不修改原数据，浅拷贝输入
            self.passangers = passangers[:] # 可变类型，为了不修改原数据，浅拷贝输入
            
    def pick(self, name):
        self.passangers.append(name)
    
    def drop(self, name):
        self.passangers.drop(name)
    

student_list = ['abby', 'bob', 'wang']
school_bus = BusMoving(student_list)
school_bus.pick('cindy')
print(student_list)
print(school_bus.passangers)
