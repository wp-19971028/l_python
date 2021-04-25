import socket
def send_file_2_client(new_client_socket,client_addr):
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端%s要下载的文件是:%s" % (str(client_addr), file_name))
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)"%file_name)
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1. 买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(("", 9028))

    # 3. 将手机设置为正常的 响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    while True:
    # 4. 等待别人的电话到来(等待客户端的链接 accept)
        new_client_socket, client_addr = tcp_server_socket.accept()
        send_file_2_client(new_client_socket,client_addr)
        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
