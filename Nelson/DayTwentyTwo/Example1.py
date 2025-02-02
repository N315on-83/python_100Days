import json

# 1. 创建一个字典对象
my_dict = {
    'name': '张三',
    'age': 30,
    'friends': ['李四', '王五'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 300}
    ]
}

# 2. 将字典转为 JSON 格式字符串（序列化）
json_str = json.dumps(my_dict, ensure_ascii=False, indent=4)  # ensure_ascii=False 保证中文不转义
print("JSON 格式的字符串:")
print(json_str)

# 3. 将字典转化为 JSON 并写入文件（序列化）
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(my_dict, file, ensure_ascii=False, indent=4)  # 写入文件

print("\nJSON 数据已写入文件 'data.json'")

# 4. 从 JSON 文件中读取数据并反序列化为 Python 对象
with open('data.json', 'r', encoding='utf-8') as file:
    loaded_dict = json.load(file)  # 反序列化
    print("\n从文件加载的字典数据:")
    print(loaded_dict)

# 5. 从 JSON 格式字符串反序列化为 Python 对象
json_str = '{"name": "李四", "age": 28, "friends": ["王五", "赵六"], "cars": [{"brand": "Tesla", "max_speed": 250}]}'
loaded_dict_from_str = json.loads(json_str)  # 从字符串反序列化
print("\n从 JSON 字符串加载的字典数据:")
print(loaded_dict_from_str)
