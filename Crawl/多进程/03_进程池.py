# 减少资源消耗，使资源复用
import multiprocessing
import time

def square(data):
    time.sleep(1)
    result=data*data
    return result

if __name__ == '__main__':
    inputs=list(range(100))
    s=time.time()
    pool=multiprocessing.Pool(processes=4)  # 池子中存在四个进程
    # map把任务交给进程池，inputs里面的参数挨个送给square函数
    pool_outputs=pool.map(square,inputs)
    # 执行一个任务（只有一个参数时）
    # pool_outputs=pool.apply(square,args=(15,))
    pool.close()    # 关闭进程池
    pool.join() # 堵塞进程，所有进程执行完毕再向下执行
    e=time.time()
    print('Pool:',pool_outputs)
    print("共耗时{}秒".format(e-s))
