from multiprocessing import  Process,Queue

def write(q):
    print("Process to write:%s"%Process.pid)
    for i in range(10):
        print("Put %d to queue..."%i)
        q.put(i)    # 入队

def read(q):
    print("Process to read:%s"%Process.pid)
    while True:
        value=q.get()   # 取队顶元素
        print("Read %d from queue..."%value)

if __name__ == '__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()   # 确保数据全部进队之后再读出

