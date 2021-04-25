from socket import *
# 创建socket
tcp_sever_socket = socket(AF_INET,SOCK_STREAM)
# 绑定
tcp_sever_socket.bind(("",7878))
# 使用socket创建套接字默认的属性是主动的
# 使用listen可以将其变为被动
# 这样就可以接收别人的链接了
tcp_sever_socket.listen(128)
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
client_socket,chient_Addr = tcp_sever_socket.accept()
# 接收对方发来的数据
recv_data = client_socket.recv(1024) #接收1024个字节
print("接收到的数据为:",recv_data.decode("gbk"))

# 发送一些数据到客户端
client_socket.send("谢谢!!! ".encode("gbk"))

# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
client_socket.close()