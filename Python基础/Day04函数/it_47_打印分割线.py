def print_line(char, times):
    """
    打印一次分割线
    :param char: 指定字符串
    :param times: 指定长度
    :return: null
    """
    print(char * times)





def print_lines(i, char, times):
    """
    打印n次分割线
    :param i: 打印次数
    :param char: 指定打印字符串
    :param times: 字符长度
    :return: null
    """
    row = 0
    while row < i:
        print_line(char, times)
        row += 1

