# I/O密集型用多线程
import threading
import time

def start():
    time.sleep(5)
    print(threading.current_thread().name)  # 当前线程的名字
    print(threading.current_thread().isAlive()) # 当前线程是否还活着
    print(threading.current_thread().ident) # 当前线程的id

if __name__ == '__main__':
    print('start')
    # target=函数名，不用加()，否则表示实例化会有返回值
    t=threading.Thread(target=start,name='my first thread') # name为线程名字，有默认值可以省略
    # 不加setDaemon(True)为非守护线程
    # 非守护线程——即使主程序结束，程序也会等待线程完成之后停止

    t.setDaemon(True)   # 守护线程——线程随着主程序的结束而结束

    t.start()   # 启动线程
    t.join()    # 堵塞线程，线程结束后再向下执行
    print('stop')
