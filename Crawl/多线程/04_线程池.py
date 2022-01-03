# pip install threadpool
import time
import threadpool

i=1
# 执行比较耗时的函数，需要开启多线程
def get_html(url):
    global i
    time.sleep(3)   # 假设获取一个页面需要3s
    print("第%d个页面返回成功..."%i)
    i+=1

if __name__ == '__main__':
    urls=[i for i in range(10)] # 假设十个url
    s=time.time()
    pool=threadpool.ThreadPool(10)  # 建立线程池，可并行执行10个线程（宏观）
    # 提交任务给线程池
    requests=threadpool.makeRequests(get_html,urls) # 函数，参数
    # 开始执行
    for req in requests:
        pool.putRequest(req)
    pool.wait() # 等待所有线程任务都完成
    e=time.time()
    print("共耗时{}".format(e-s))
