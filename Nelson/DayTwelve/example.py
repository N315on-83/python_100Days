import re

def validate_user_input():
    username = input("请输入用户名: ")
    qq = input("请输入QQ号: ")
    
    # 验证用户名：由字母、数字或下划线构成，长度在6~20个字符之间
    # 正则：^[0-9a-zA-Z_]{6,20}$
    if re.match(r'^[0-9a-zA-Z_]{6,20}$', username):
        print(f"用户名 '{username}' 格式正确!")
    else:
        print(f"用户名 '{username}' 格式不正确，请检查后重新输入。")

    # 验证QQ号：5~12位数字且首位不能是0
    # 正则：^[1-9]\d{4,11}$
    if re.match(r'^[1-9]\d{4,11}$', qq):
        print(f"QQ号 '{qq}' 格式正确!")
    else:
        print(f"QQ号 '{qq}' 格式不正确，请检查后重新输入。")

if __name__ == "__main__":
    validate_user_input()
