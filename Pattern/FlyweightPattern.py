"""
享元模式：通过共享尽可能多的相似对象来最小化内存使用和提高性能

享元（Flyweight）： 代表具有共享状态的对象。它包含了内部状态和外部状态，内部状态是可以共享的，而外部状态是对象的上下文信息，需要在对象外部进行管理。
享元工厂（Flyweight Factory）： 负责创建和管理享元对象。它通常包含一个享元池，用于存储和获取享元对象，并确保共享对象的唯一性。
"""
class Shape:
    def draw(self, x, y):
        pass

class Circle(Shape):
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):  # x,y 外部非享元状态
        print(f"Drawing a {self.color} circle at position ({x}, {y})")

class ShapeFactory:
    _shapes = {}

    def get_circle(self, color):
        if color not in self._shapes:
            self._shapes[color] = Circle(color)
        return self._shapes[color]

class DrawingApp:
    def __init__(self):
        self.shapes = []
        self.factory = ShapeFactory()

    def draw_circle(self, color, x, y):
        circle = self.factory.get_circle(color)
        circle.draw(x, y)
        self.shapes.append(circle)

if __name__ == "__main__":
    app = DrawingApp()

    # 绘制多个圆形，并指定颜色和位置
    app.draw_circle('red', 10, 15)
    app.draw_circle('blue', 20, 25)
    app.draw_circle('red', 30, 35)
    app.draw_circle('green', 40, 45)