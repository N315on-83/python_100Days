import pandas as pd

# 读取原始 CSV 文件
file_path = '/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentyThree/Nigerian_Car_Prices.csv'
df = pd.read_csv(file_path)

# 确保里程列名称正确，这里假设是 'Mileage'
# 按照 'Mileage' 列进行排序，降序排列
df_sorted = df.sort_values(by='Mileage', ascending=False)

# 打印排序后的数据
print(df_sorted)

# 保存排序后的数据到新的 CSV 文件
output_path = '/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentyThree/Nigerian_Car_Prices_Sorted.csv'
df_sorted.to_csv(output_path, index=False)

print(f"Sorted data saved to: {output_path}")
