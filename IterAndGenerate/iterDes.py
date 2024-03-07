import re
import reprlib

"""
可迭代对象（Iterable）是实现了__iter__()方法的对象，通过调用iter()方法可以获得一个迭代器（Iterator）。
迭代器（Iterator）是实现了__iter__()方法和__next()__方法的对象。
for...in...的迭代实际是将可迭代对象转换成迭代器，再重复调用next()方法实现的。
生成器（Generator）是一个特殊的迭代器，它的实现更简单优雅。
yield是生成器实现__next__()方法的关键。它作为生成器执行的暂停恢复点，可以对yield表达式进行赋值，也可以将yield表达式的值返回。
"""
RE_WORD = re.compile('\w+')


# from collections.abc import Iterator
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):  # 实现__getitem__方法称为可迭代对象
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class Sentence2:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return SentenceIterator(self.words)  # 返回一个迭代器


class SentenceIterator:  # 迭代器
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):  # 迭代器要实现next方法
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):  # 迭代器iter魔术方法返回其本生
        return self


class Sentence3:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # 生成器
        for word in self.words:
            yield word


class Sentence4:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # 生成器
        for match in RE_WORD.findall(self.text):
            yield match.group()


class Sentence5:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))  # 生成器表达式


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None 无穷数列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index  # 等差数列


def arithmetic_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    index = 0
    forever = end is None
    while forever or index < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == "__main__":
    for i in ArithmeticProgression(1, 1, 10):
        print(i)
