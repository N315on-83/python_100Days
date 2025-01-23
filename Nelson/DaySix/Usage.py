# 换行符：\n 是转义字符，表示换行
print("Hello\nWorld")  # 输出：
# Hello
# World

# 制表符：\t 是转义字符，表示制表符（类似于一个 Tab 键）
print("Hello\tWorld")  # 输出：
# Hello   World  （"Hello" 和 "World" 之间有空白，类似 Tab 键）

# 反斜杠：\\ 是转义字符，表示单个反斜杠（因为反斜杠是转义符号，所以需要用两个反斜杠来表示一个）
print("C:\\Users\\Name")  # 输出：
# C:\Users\Name  （显示路径时需要用双反斜杠）

# 单引号：\' 是转义字符，表示单引号（用来避免与字符串的单引号结束符冲突）
print('It\'s a book')  # 输出：
# It's a book  （输出包含了单引号）

# 双引号：\" 是转义字符，表示双引号（用来避免与字符串的双引号开始符冲突）
print("He said, \"Hello!\"")  # 输出：
# He said, "Hello!"  （输出包含了双引号）
