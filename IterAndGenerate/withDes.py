"""

"""
import contextlib


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'
    
    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

with LookingGlass() as saywhat:
    print("ssasfdsag")
    print(saywhat)
print(saywhat)


@contextlib.contextmanager  # 使用 @contextmanager 装饰的生成器。 yield把函数分成两部分。对应__enter__和__exit__
def looking_glass():
    import sys
    original_write = sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write