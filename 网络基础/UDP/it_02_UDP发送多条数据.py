import socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 准备接收方数据地址
dest_addr = ('192.168.0.103',8080) # 注意 是元组，ip是字符串，端口是数字

# 从键盘获取数据
send_data = input("请输入您要发送的数据:")
# 发送数据到指定的电脑
udp_socket.sendto(send_data.encode('gbk'),dest_addr)
# 关闭套接字

# 等待对方发送数据并接受
recv_data = udp_socket.recvfrom(1024) # 1024表示本次接收的最大字节数

# 6. 显示对方发送的数据
# 接收到的数据recv_data是一个元组
# 第1个元素是对方发送的数据
# 第2个元素是对方的ip和端口
print(recv_data[0].decode("gbk"))
print(recv_data[1])
udp_socket.close()