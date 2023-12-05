"""
Python代码的执行是由Python虚拟机进行控制。它在主循环中同时只能有一个控制线程在执行，
Python解释器中可以运行多个线程，但是在执行的只有一个线程，其他的处于等待状态。

这些线程执行是有全局解释器锁（GIL）控制，它来保证同时只有一个线程在运行。在多线程运行环境中，Python虚拟机执行方式如下：
1:设置GIL
2:切换进线程
3：执行下面操作之一
    3.1：运行指定数量的字节码指令
    3.2：线程主动让出控制权
4：切换出线程（线程处于睡眠状态）
5：解锁GIL
6:进入1步骤
注意：Python运行计算密集型的多线程程序时，更倾向于让线程在整个时间片内始终占据GIL，而I/O秘籍型的多线程程序在I/O被调用前会释放GIL，以允许其他线程在I/O执行的时候运行。
"""
import threading

mylock = threading.RLock()
num = 0


class WorkThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('\n%s locked, number: %d' % (self.t_name, num))
            if num >= 2:
                mylock.release()
                print('\n%s released, number: %d' % (self.t_name, num))
                break
            num += 1
            print('\n%s released, number: %d' % (self.t_name, num))
            mylock.release()


def test():
    thread1 = WorkThread('A-Worker')
    thread2 = WorkThread('B-Worker')
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    test()
