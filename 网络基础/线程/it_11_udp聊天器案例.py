import socket
import threading


def recv_msg(udp_socket):
    """接收数据并显示"""

    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    # 发送数据
    while True:
        send_data = input("输入要发送的数据:")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


def main():
    """完成udp聊天器的整体控制"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("", 8888))
    # 获取对方IP
    dest_ip = input("请输入对方的IP地址:")
    dest_port = int(input("请输入对方端口:"))
    # 创建两个线程去执行相应功能
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
