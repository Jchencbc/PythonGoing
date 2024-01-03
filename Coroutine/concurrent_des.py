"""
介绍 concurrent.futures 模块
主要实现了进程池和线程池，适合做派生一堆任务，异步执行完成后，再收集这些任务，且保持相同的api
"""

"""
Executor
ThreadPoolExecutor(max_workers=None)  线程池构建
ProcessPoolExecutor(max_workers=None)  进程池构建
max_workers 池大小
方法：
map(func,*iterables,timeout=None,chunksize=1)  内置map很像，对序列执行相同操作，是异步执行的、非阻塞。返回的是一个生成器，可以遍历该生成器得到结果
submit(fn,/,*args,**kwargs)  将fn加入池中，以 fn(*args **kwargs) 方式执行并返回Future对象封装该函数的执行。
shutdown(wait=True,*,cancel_futures=False)  关闭释放资源，可以使用with语句避免显示调用
"""
from concurrent import futures
import time
import random

def returnNumber(number: int) -> int:
    print("start threading {}".format(number))
    time.sleep(random.randint(0, 2))  # 随机睡眠
    print("end threading {}".format(number))
    return number  # 返回参数本身

if __name__ == '__main__':
    with futures.ThreadPoolExecutor(3) as executor:
        # with语句会调用executor.shutdown(wait=True)，在所有线程都执行完毕前阻塞当前线程
        res = executor.map(returnNumber,range(0, 5))
        # 返回一个生成器，遍历的结果为0,1,2,3。无论执行结果先后顺序如何，看输入的iterator顺序
        # 因为线程池为3，所以0~2进池，其中某个执行完后，3进池
        print(res)
    print("----print result----")
    for r in res:
        print(r)