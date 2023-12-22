from asyncio import QueueEmpty
from multiprocessing import Manager, Pipe, Pool, Process, Queue
import random
import time
import os

"""
process模块
"""

# def info():
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info()
#     time.sleep(3)
#     print('hello', name)

# if __name__ == '__main__':
#     info()
#     p = Process(target=f, args=('bob',))
#     p.daemon = True  # 守护进程
#     print(p.daemon)
#     p.start()
#     p.join(1)
#     print('name:', p.name)  # 进程名
#     print('is_alive:', p.is_alive())  # 判断进程是否存活
#     print('exitcode:', p.exitcode)
    
    
"""
进程通信之 pipe & queue
"""
# def son_process(x, pipe):
#     _out_pipe, _in_pipe = pipe

#     # 关闭fork过来的输入端
#     _in_pipe.close()
#     while True:
#         try:
#             msg = _out_pipe.recv()
#             print(msg)
#         except EOFError:
#             # 当out_pipe接受不到输出的时候且输入被关闭的时候，会抛出EORFError，可以捕获并且退出子进程
#             break


# if __name__ == '__main__':
#     out_pipe, in_pipe = Pipe(True)  # 主进程数据通道 输出和输入
#     son_p = Process(target=son_process, args=(100, (out_pipe, in_pipe)))  # 子进程fork主进程的双向通道  
#     son_p.start()

#     # 等 pipe 被 fork 后，关闭主进程的输出端
#     # 这样，创建的Pipe一端连接着主进程的输入，一端连接着子进程的输出口
#     out_pipe.close()
#     for x in range(1000):
#         in_pipe.send(x)
#     in_pipe.close()
#     son_p.join()
#     print("主进程也结束了")


# def getter(name, queue):
#     print('Son process %s' % name)
#     while True:
#         try:
#             value = queue.get(True, 10)
#             # block为True,就是如果队列中无数据了。
#             #   |—————— 若timeout默认是None，那么会一直等待下去。
#             #   |—————— 若timeout设置了时间，那么会等待timeout秒后才会抛出Queue.Empty异常
#             # block 为False，如果队列中无数据，就抛出Queue.Empty异常
#             print("Process getter get: %f" % value)
#         except QueueEmpty:
#             break


# def putter(name, queue):
#     print("Son process %s" % name)
#     for i in range(0, 1000):
#         value = random.random()
#         queue.put(value)
#         # 放入数据 put(obj[, block[, timeout]])
#         # 若block为True，如队列是满的：
#         #  |—————— 若timeout是默认None，那么就会一直等下去
#         #  |—————— 若timeout设置了等待时间，那么会等待timeout秒后，如果还是满的，那么就抛出Queue.Full.
#         # 若block是False，如果队列满了，直接抛出Queue.Full
#         print("Process putter put: %f" % value)


# if __name__ == '__main__':
#     queue = Queue()
#     getter_process = Process(target=getter, args=("Getter", queue))
#     putter_process = Process(target=putter, args=("Putter", queue))
#     getter_process.start()
#     putter_process.start()

"""
进程间数据共享
"""
# def fun1(dic,lis,index):

#     dic[index] = 'a'
#     dic['2'] = 'b'    
#     lis.append(index)    #[0,1,2,3,4,0,1,2,3,4,5,6,7,8,9]
#     #print(l)

# if __name__ == '__main__':
#     with Manager() as manager:
#         dic = manager.dict()  #注意字典的声明方式，不能直接通过{}来定义
#         l = manager.list(range(5))#[0,1,2,3,4]

#         process_list = []
#         for i in range(10):
#             p = Process(target=fun1, args=(dic,l,i))
#             p.start()
#             process_list.append(p)

#         for res in process_list:
#             res.join()
#         print(dic)
#         print(l)


"""
pool模块
进程池中有可用进程为止。就是固定有几个进程可以使用。
apply：同步，一般不使用
apply_async：异步
map
map_async
"""

def fun_01(i):
    time.sleep(2)
    print('start_time:', time.ctime())
    return i + 100
 
 
def fun_02(arg):
    print('end_time:', arg, time.ctime())
 
 
if __name__ == '__main__':
    pool = Pool(3)
    for i in range(4):
        pool.apply_async(func=fun_01, args=(i,), callback=fun_02)  # fun_02的入参为fun_01的返回值
        # pool.apply_async(func=fun_01, args=(i,))
    pool.close()
    pool.join()


def run(fn):
    # fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    print(fn * fn)
 
 
if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    print('shunxu:')  # 顺序执行(也就是串行执行，单进程)
    s = time.time()
    for fn in testFL:
        run(fn)
    t1 = time.time()
    print("顺序执行时间：", int(t1 - s))
 
    print('concurrent:')  # 创建多个进程，并行执行
    pool = Pool(3)  # 创建拥有3个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    pool.map(run, testFL)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
