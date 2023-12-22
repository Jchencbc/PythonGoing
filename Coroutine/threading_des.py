import threading
from threading import Lock,Thread
import time,os


'''
线程也叫轻量级进程，是操作系统能够进行运算调度的最小单位，它被包涵在进程之中，是进程中的实际运作单位。
线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个进程的其他线程共享进程所
拥有的全部资源。一个线程可以创建和撤销另一个线程，同一个进程中的多个线程之间可以并发执行
'''

'''
线程在程序中是独立的、并发的执行流。与分隔的进程相比，进程中线程之间的隔离程度要小，它们共享内存、文件句柄
和其他进程应有的状态。
因为线程的划分尺度小于进程，使得多线程程序的并发性高。进程在执行过程之中拥有独立的内存单元，而多个线程共享
内存，从而极大的提升了程序的运行效率。
线程比进程具有更高的性能，这是由于同一个进程中的线程都有共性，多个线程共享一个进程的虚拟空间。线程的共享环境
包括进程代码段、进程的共有数据等，利用这些共享的数据，线程之间很容易实现通信。
操作系统在创建进程时，必须为改进程分配独立的内存空间，并分配大量的相关资源，但创建线程则简单得多。因此，使用多线程
来实现并发比使用多进程的性能高得要多。
'''

'''
进程之间不能共享内存，但线程之间共享内存非常容易。
操作系统在创建进程时，需要为该进程重新分配系统资源，但创建线程的代价则小得多。因此使用多线程来实现多任务并发执行比使用多进程的效率高
python语言内置了多线程功能支持，而不是单纯地作为底层操作系统的调度方式，从而简化了python的多线程编程。
'''

'''
自定义线程：继承threading.Thread来定义线程类，其本质是重构Thread类中的run方法
'''
# class MyThread(threading.Thread):
#     def __init__(self,n):
#         super(MyThread,self).__init__()   #重构run函数必须写
#         self.n = n
#
#     def run(self):
#         print('task',self.n)
#         time.sleep(1)
#         print('2s')
#         time.sleep(1)
#         print('1s')
#         time.sleep(1)
#         print('0s')
#         time.sleep(1)
#
# if __name__ == '__main__':
#     t1 = MyThread('t1')
#     t2 = MyThread('t2')
#     t1.start()
#     t2.start()


'''
守护线程
下面这个例子，这里使用setDaemon(True)把所有的子线程都变成了主线程的守护线程
'''
# def run(n):
#     print('task',n)
#     time.sleep(1)
#     print('3s')
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#
# if __name__ == '__main__':
#     t=threading.Thread(target=run,args=('t1',))
#     t.setDaemon(True)
#     t.start()
#     print('end')
'''
通过执行结果可以看出，设置守护线程之后，当主线程结束时，子线程也将立即结束，不再执行
'''

'''
主线程等待子线程结束
为了让守护线程执行结束之后，主线程再结束，我们可以使用join方法，让主线程等待子线程执行
'''
# def run(n):
#     print('task',n)
#     time.sleep(2)
#     print('5s')
#     time.sleep(2)
#     print('3s')
#     time.sleep(2)
#     print('1s')
# if __name__ == '__main__':
#     t=threading.Thread(target=run,args=('t1',))
#     t.setDaemon(True)    #把子线程设置为守护线程，必须在start()之前设置
#     t.start()
#     t.join()     #设置主线程等待子线程结束
#     print('end')


'''
多线程共享全局变量
线程时进程的执行单元，进程时系统分配资源的最小执行单位，所以在同一个进程中的多线程是共享资源的
'''
# g_num = 100
# def work1():
#     global  g_num
#     for i in range(3):
#         g_num+=1
#     print('in work1 g_num is : %d' % g_num)
#
# def work2():
#     global g_num
#     print('in work2 g_num is : %d' % g_num)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=work1)
#     t1.start()
#     time.sleep(1)
#     t2=threading.Thread(target=work2)
#     t2.start()


'''
    由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，当多个线程同时修改同一条数据时可能会出现脏数据，
所以出现了线程锁，即同一时刻允许一个线程执行操作。线程锁用于锁定资源，可以定义多个锁，像下面的代码，当需要独占
某一个资源时，任何一个锁都可以锁定这个资源，就好比你用不同的锁都可以把这个相同的门锁住一样。
    由于线程之间是进行随机调度的，如果有多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，
我们因此也称为“线程不安全”。
    为了防止上面情况的发生，就出现了互斥锁（Lock）
'''
# num = 0

# def show(arg):
#     time.sleep(i)
#     lock.acquire()
#     global num
#     num +=1
#     print('bb :{}'.format(num))
#     lock.release()

# for i in range(5):
#     t = threading.Thread(target=show, args=(i,))  # 注意传入参数后一定要有【，】逗号
#     t.start()

# print('main thread stop')



'''
递归锁：RLcok类的用法和Lock类一模一样，但它支持嵌套，在多个锁没有释放的时候一般会使用RLock类
'''
# import threading
# mylock = threading.RLock()
# num = 0
# class WorkThread(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.t_name = name
#     def run(self):
#         global num
#         while True:
#             mylock.acquire()
#             print('\n%s locked, number: %d' % (self.t_name, num))
#             if num >= 2:
#                 mylock.release()
#                 print('\n%s released, number: %d' % (self.t_name, num))
#                 break
#             num += 1
#             print('\n%s released, number: %d' % (self.t_name, num))
#             mylock.release()
# def test():
#     thread1 = WorkThread('A-Worker')
#     thread2 = WorkThread('B-Worker')
#     thread1.start()
#     thread2.start()
# if __name__ == '__main__':
#     test() 

'''
Condition被称为条件变量,除了acquire和release方法外，还提供了wait和notify方法。

首先acquire一个条件变量，然后判断一些条件。
如果条件不满足则wait；
如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。
不断的重复这一过程，从而解决复杂的同步问题。

经典问题是生产者与消费者问题
'''
# count = 0
# con = threading.Condition()
# class Producer(Thread):
    
#     def run(self):
#         global count
#         while True:
#             con.acquire()  # 条件锁
#             if count < 1000:
#                 count += 100
#                 print('producer count is {} now'.format(count))
#                 con.notify()  # 通知其他阻塞线程
#             else:
#                 con.wait()  # 条件不满足线程阻塞，等待获取锁
#             con.release()   # 释放锁
#             time.sleep(1)
                

# class Consumer(Thread):
    
#     def run(self):
#         global count
#         while True:
#             con.acquire()
#             if count > 100:
#                 count -= 30
#                 print('consumer count is {} now'.format(count))
#                 con.notify()
#             else:
#                 con.wait()
#             con.release()
#             time.sleep(1)

# def test():
#     for i in range(2):
#         p = Producer()
#         p.start()
#     for i in range(5):
#         c = Consumer()
#         c.start()
# if __name__ == '__main__':
#     test()





'''
信号量（BoundedSemaphore类）
互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据，比如厕所有3个坑，
那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去
'''
# def run(n,semaphore):
#     semaphore.acquire()   #加锁
#     time.sleep(3)
#     print('run the thread:%s\n' % n)
#     semaphore.release()    #释放


# if __name__== '__main__':
#     num=0
#     semaphore = threading.BoundedSemaphore(5)   #最多允许5个线程同时运行
#     for i in range(22):
#         t = threading.Thread(target=run,args=('t-%s' % i,semaphore))
#         t.start()
#     while threading.active_count() !=1:
#         pass
#     else:
#         print('----------all threads done-----------')

'''
python线程的事件用于主线程控制其他线程的执行，事件是一个简单的线程同步对象，其主要提供以下的几个方法：
clear将flag设置为 False
set将flag设置为 True
is_set判断是否设置了flag
wait会一直监听flag，如果没有检测到flag就一直处于阻塞状态
事件处理的机制：全局定义了一个Flag，当Flag的值为False，那么event.wait()就会阻塞，当flag值为True，
那么event.wait()便不再阻塞
'''
# event = threading.Event()
# def lighter():
#     count = 0
#     event.set()         #初始者为绿灯
#     while True:
#         if 5 < count <=10:
#             event.clear()  #红灯，清除标志位
#             print("\33[41;lmred light is on...\033[0m]")
#         elif count > 10:
#             event.set()    #绿灯，设置标志位
#             count = 0
#         else:
#             print('\33[42;lmgreen light is on...\033[0m')

#         time.sleep(1)
#         count += 1


# def car(name):
#     while True:
#         if event.is_set():     #判断是否设置了标志位
#             print('[%s] running.....'%name)
#             time.sleep(1)
#         else:
#             print('[%s] sees red light,waiting...'%name)
#             event.wait()
#             print('[%s] green light is on,start going...'%name)


# # startTime = time.time()
# light = threading.Thread(target=lighter,)
# light.start()

# car = threading.Thread(target=car,args=('MINT',))
# car.start()
# endTime = time.time()
# # print('用时：',endTime-startTime)

'''
有些变量初始化以后，我们只想让他们在每个线程中一直存在，相当于一个线程内的共享变量，线程之间又是隔离的。 
python threading模块中就提供了这么一个类，叫做local。
local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。、

三、threading.local() 类的使用场景
这时候，大家也许会比较迷惑，
如果需要数据隔离，使用局部变量，
如果需要共享数据并同步，使用全局变量加锁就好了呀！
为什么要有一个thread-local 数据？为什么要用 local() 类？local() 类，有什么使用场景呢？

在多线程环境下，每个线程都有自己的数据。
所以，当我们使用线程的时候，能用线程的局部变量，就尽量不要用全局变量。
因为使用全局变量涉及数据同步的问题，对于全局变量的修改必须加锁，保持各个线程中的数据同步。

但是，有时候使用局部变量也不太方便。
比如，多线程中涉及函数调用时，
如果使用局部变量，那么必须通过参数传递变量；
这时候如果使用全局变量也不行，因为每个线程处理的对象不同。

这时候，使用 threading.local，就能发挥出作用了。
在全局作用域，通过实例化 threading.local 类，得到一个 thread-local 数据对象，该thread-local 数据即为一个全局变量，但是每个线程却可以利用它来保存属于自己的私有属性，这些私有属性对其他线程也是不可见的。
通过调用全局对象的私有属性，自动获取当前线程对应的属性值，使代码更优雅简洁！
'''
import threading

# Threading.local对象
localManager = threading.local()  # 全局类
localManager.num = 100  # d
lock = threading.RLock()

class MyThead(threading.Thread):
    def __init__(self, threadName, name):
        super(MyThead, self).__init__(name=threadName)
        self.__name = name

    def run(self):
        global localManager
        localManager.ThreadName = self.name
        localManager.Name = self.__name
        MyThead.ThreadPoc()
    # 线程处理函数
    @staticmethod
    def ThreadPoc():
        lock.acquire()
        try:
            print('Thread={id}'.format(id=localManager.ThreadName))
            print('Name={name}'.format(name=localManager.Name))
        finally:
            lock.release()

if __name__ == '__main__':
    bb = {'Name': 'bb'}
    aa = {'Name': 'aa'}
    xx = (aa, bb)
    threads = [MyThead(threadName='id_{0}'.format(i), name=xx[i]['Name']) for i in range(len(xx))]
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
