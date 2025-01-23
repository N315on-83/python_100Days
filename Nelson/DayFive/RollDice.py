from random import randint  # 导入 randint 模块，用于生成随机整数

def roll_dice(n=2):
    """摇色子"""
    total = 0  # 初始化总和为 0
    for _ in range(n):  # 循环 n 次，每次模拟摇一个色子
        total += randint(1, 6)  # 摇一个色子，得到 1 到 6 之间的随机数，并累加到 total 上
    return total  # 返回色子摇出的总和

def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c  # 返回三个参数的和，若没有传参，则使用默认值 0

# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())  # 调用 roll_dice 函数，默认摇两颗色子，输出两颗色子的和
# 摇三颗色子
print(roll_dice(3))  # 调用 roll_dice 函数，指定摇三颗色子，输出三颗色子的和

print(add())  # 调用 add 函数，默认三个数相加，输出 0 + 0 + 0
print(add(1))  # 调用 add 函数，只传递第一个参数 1，输出 1 + 0 + 0
print(add(1, 2))  # 调用 add 函数，传递前两个参数 1 和 2，输出 1 + 2 + 0
print(add(1, 2, 3))  # 调用 add 函数，传递所有三个参数 1, 2, 3，输出 1 + 2 + 3

# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))  # 使用命名参数，指定 c=50, a=100, b=200，输出 100 + 200 + 50
