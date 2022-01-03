# with——自动打开自动关闭
import threading
import time

class Test:
    rlock=threading.RLock()
    def __init__(self):
        self.number=0

    def execute(self,n):
        with Test.rlock:
            self.number+=n

    def add(self):
        with Test.rlock:
            self.execute(1)

    def down(self):
        with Test.rlock:
            self.execute(-1)

def add(test):
    for i in range(1000000):
        test.add()
def down(test):
    for i in range(1000000):
        test.down()

if __name__ == '__main__':
    t=Test()
    # args为参数，传给target所指的函数
    t1=threading.Thread(target=add,args=(t,))
    t2=threading.Thread(target=down,args=(t,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(t.number)
