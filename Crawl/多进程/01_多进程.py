# 计算密集型用多进程
import multiprocessing
import time

def start(i):
     time.sleep(1)
     print(i)
     print(multiprocessing.current_process().name)  # 当前进程的名字
     print(multiprocessing.current_process().pid)   # 当前进程的pid
     print(multiprocessing.current_process().is_alive())    # 当前进程是否活着

if __name__ == '__main__':
    print('start')
    p=multiprocessing.Process(target=start,args=(1,))
    p.start()
    # 不加join，会直接执行到stop，之后等待进程结束
    p.join()
    print('stop')