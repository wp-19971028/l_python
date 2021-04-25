import socket


# 定义发送数据的函数
def send_mas(udp_socket):
    """
    获取键盘输入数据并发送给对方
    :param udp_socket:
    :return:
    """
    # 从键盘输入数据
    msg = input("\n请输入你要发送的数据:")
    # 输入对方的IP地址及端口
    dest_ip = input("\n请输入对方的IP地址")
    dest_port = int(input("\n请输入对方的端口"))
    # 发送数据
    udp_socket.sendto(msg.encode("gbk"), (dest_ip,dest_port))


# 定义接收数据的函数
def recv_msg(udp_socket):
    """接收数据并显示"""
    # 接收数据
    recv_msg = udp_socket.recvfrom(1024)
    # 解码
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode("gbk")
    print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("", 7878))
    # 逻辑编写
    while True:
        # 选择功能
        print("-" * 30)
        print("1 :发送消息")
        print("2 :接收消息")
        print("-" * 30)
        op_num = input("请输入要操作的功能序号:")
        # 根据选择调用相应的函数
        if op_num == "1":
            send_mas(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("输入有误请重新输入......")


if __name__ == "__main__":
    main()
