# 输入苹果单价
price_str = input("输入苹果的电价:")
# 输入苹果的重量
weight_str = input("输入苹果的重量:")
# 计算支付的金额
# 1> 将价格和重量转换成小数
price = float(price_str)
weight = float(weight_str)
money = price * weight
# 计算支付金额
print("请支付:",money)