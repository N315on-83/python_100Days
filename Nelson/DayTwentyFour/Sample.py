import pandas as pd 

# 读取 Excel 文件
raw_data = pd.read_excel('/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentyFour/random_data.xlsx')

# 计算 D 列（Price）的中位数
median_price = raw_data["Quantity"].median()

# 输出结果
print("D列（Price）的中位数:", median_price)
