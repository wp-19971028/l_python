from socket import *

# 创建socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
# 目的信息
sever_ip = input("输入服务器ip:")
sever_port = int(input("输入服务器port:"))
# 链接服务器
tcp_client_socket.connect((sever_ip, sever_port))
# 提示用户输入数据
send_data = input("请输入要发送的数据:")
tcp_client_socket.send(send_data.encode("gbk"))
# 接受对方发送的数据,最大1024个字节
recvData = tcp_client_socket.recv(1024)
print("接收的数据为:", recvData.decode("gbk"))

# 关闭套接字
tcp_client_socket.close()
