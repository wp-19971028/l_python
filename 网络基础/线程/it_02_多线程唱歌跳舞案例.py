from time import sleep, ctime
import threading


def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    # sing()
    # dance()
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
# 可以明显看出使用了多线程并发的操作，花费时间要短很多
# 可以并发执行
# 当调用start()时，才会真正的创建线程，并且开始执行
    print('---结束---:%s' % ctime())




















