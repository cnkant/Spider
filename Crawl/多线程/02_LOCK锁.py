'''
import threading
number=0
def addNumber():
    global number
    for i in range(1000000):
        number+=1
        # 运行时分为计算赋值两步：a=number+1，number=a

def downNumber():
    global number
    for i in range(1000000):
        number-=1
        # 运行时分为计算赋值两步：b=number-1，number=b

if __name__ == '__main__':
    print('start')
    t=threading.Thread(target=addNumber)
    t2=threading.Thread(target=downNumber)
    t.start()
    t2.start()
    t.join()
    t2.join()
    print(number)
    print('stop')
# 由于CPython的GIL锁，导致计算和赋值操作分开，最终输出的number值为一个不确定的数
'''
# 解决方法是添加LOCK锁——多线程同时争夺统一资源时使用
# LOCK锁一个进程使用后必须释放，否则其他进程无法执行会一直等待
import threading
lock=threading.Lock()  # 创建一个锁
number=0
def addNumber():
    global number
    for i in range(1000000):
        # 加锁可以保证一次计算和赋值操作完成后再让出资源
        lock.acquire() # 上锁
        number+=1
        lock.release()  # 释放锁

def downNumber():
    global number
    for i in range(1000000):
        lock.acquire()
        number-=1
        lock.release()

if __name__ == '__main__':
    print('start')
    t=threading.Thread(target=addNumber)
    t2=threading.Thread(target=downNumber)
    t.start()
    t2.start()
    t.join()
    t2.join()
    print(number)
    print('stop')
