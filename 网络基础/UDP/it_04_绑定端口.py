import socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
local_daar = ("",7878) #  ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udp_socket.bind(local_daar)
# 等待接收对方发送数据
recv_data = udp_socket.recvfrom(1024)
# 显示接收数据
print(recv_data[0].decode("gbk"))

# 关闭套接字

udp_socket.close()