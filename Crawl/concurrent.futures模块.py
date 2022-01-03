# # concurrent是异步的线程、进程包
# submit(function,argument)：调度函数（可调用的对象）的执行，将argument作为参数传入
# map(function,argument)：将argument作为参数执行函数，以异步的方式
# from concurrent.futures import ThreadPoolExecutor(max_workers)    # 线程池
# from concurrent.futures import ProcessPoolExecutor(max_workers)   # 进程池
# max_workers 表示最多可并行执行多少任务
import concurrent.futures
import time

number_list=[i for i in range(1,11)]
def add_item(x):
    result=count(x)
    return result
def count(number):
    for i in range(0,1000000):
        i+=1
    return i*number

if __name__ == '__main__':
    # 单线程裸奔
    s=time.time()
    for item in number_list:
        print(add_item(item))
    print(time.time()-s)

    # 线程池执行CPU密集型任务
    s2=time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures=[executor.submit(add_item,item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print(time.time()-s2)

    # 进程池执行CPU密集型任务
    s3=time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures=[executor.submit(add_item,item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print(time.time()-s3)
