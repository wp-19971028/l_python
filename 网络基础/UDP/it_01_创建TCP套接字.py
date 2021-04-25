import socket

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 这里是使用套接字的功能
pass

# 不用的时候关闭套接字
s.close()
