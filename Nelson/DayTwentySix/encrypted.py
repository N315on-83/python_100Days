import PyPDF2

# 定义原始 PDF 文件路径和加密后输出的文件路径
original_pdf = "/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentySix/practice.pdf"
encrypted_pdf = "/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentySix/practice_encrypted.pdf"

# 设置加密密码
password = "888888"  # 请将此处的密码替换为你需要的密码

# 读取原始 PDF 文件
with open(original_pdf, "rb") as in_file:
    reader = PyPDF2.PdfReader(in_file)
    writer = PyPDF2.PdfWriter()
    
    # 将原始 PDF 的每一页添加到 PdfWriter 中
    for page in reader.pages:
        writer.add_page(page)
    
    # 为 PDF 文件加密（设置用户密码）
    writer.encrypt(password)

    # 将加密后的 PDF 写入新文件
    with open(encrypted_pdf, "wb") as out_file:
        writer.write(out_file)
        
print("PDF 加密成功，生成的加密文件为：", encrypted_pdf)
