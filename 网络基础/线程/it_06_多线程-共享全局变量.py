import threading
import time

g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1
        print("----in work1, g_num is %d---" % g_num)


def work2():
    global g_num
    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

t1 = threading.Thread(target=work1)
t1.start()

# 延迟一会等待线程一做完
time.sleep(1)
print("-"*50)

t2 = threading.Thread(target=work2)
t2.start()