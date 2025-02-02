# 创建集合
my_set = {1, 2, 3, 4, 5}

# 尝试添加重复元素
my_set.add(3)  # 集合不会增加重复元素

# 成员运算
print(3 in my_set)   # 输出: True
print(6 not in my_set)  # 输出: True

# 由于无序性，集合不能通过索引访问元素
# print(my_set[0])  # 会报错

# 但是可以遍历
for item in my_set:
    print(item)
