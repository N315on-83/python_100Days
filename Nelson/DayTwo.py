year = int(input('请输入年份: '))
# 使用 // 进行整数除法，然后判断结果是否为整数
is_leap = (year // 4 == year / 4) and (year // 100 != year / 100 or year // 400 == year / 400)
print(is_leap)
2028