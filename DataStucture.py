# 元组解包
"""
_表示占位符
"""
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

# Python collections模块deque 双向队列
"""
deque是栈和队列的一种广义实现，deque是"double-end queue"的简称；
deque支持线程安全、有效内存地以近似O(1)的性能在deque的两端插入和删除元素，
尽管list也支持相似的操作，但是它主要在固定长度操作上的优化，
从而在pop(0)和insert(0,v)（会改变数据的位置和大小）上有O(n)的时间复杂度。
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# 从一个集合中获得最大或者最小的 N 个元素列表，heapq 模块有两个函数：nlargest() 和 nsmallest()
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素
"""
当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。 
仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用 min() 和 max() 函数会快。 
如果 N 的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 （ sorted(items)[:N] 或者是 sorted(items)[-N:] ）。 
"""
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)  # heap[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
heapq.heappop(heap)  # -4
heapq.heappop(heap)  # 1
heapq.heappop(heap)  # 2


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()  # Item('bar')
q.pop()  # Item('spam')
q.pop()  # Item('foo')
q.pop()  # Item('grok')

#  defaultdict&&setdefault()
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {}  # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

#  字典排序collections 模块中的 OrderedDict
from collections import OrderedDict

"""
OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
"""
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

# 字典运算
"""
zip() 函数先将键和值反转,zip() 函数创建的是一个只能访问一次的迭代器
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))  # min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))  # max_price is (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
min(prices, key=lambda k: prices[k])

# 两个字典共同点
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# Find keys in common
a.keys() & b.keys()  # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys()  # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items()  # { ('y', 2) }
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
