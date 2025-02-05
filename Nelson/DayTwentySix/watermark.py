import os
import PyPDF2

# 配置文件夹路径（请根据实际情况修改）
input_folder = "/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentySix/input_pdfs"
output_folder = "/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentySix/output_pdfs"
watermark_path = "/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentySix/watermark.pdf"

# 如果输出文件夹不存在，则创建
os.makedirs(output_folder, exist_ok=True)

# 读取水印 PDF（假设水印 PDF 的第一页是水印页面）
with open(watermark_path, "rb") as wm_file:
    watermark_reader = PyPDF2.PdfReader(wm_file)
    watermark_page = watermark_reader.pages[0]

# 遍历输入文件夹中的所有 PDF 文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        input_pdf_path = os.path.join(input_folder, filename)
        output_pdf_path = os.path.join(output_folder, filename)

        # 打开并读取原始 PDF
        with open(input_pdf_path, "rb") as in_file:
            reader = PyPDF2.PdfReader(in_file)
            writer = PyPDF2.PdfWriter()

            # 对每一页添加水印
            for page in reader.pages:
                # 将水印页面合并到当前页面上
                page.merge_page(watermark_page)
                writer.add_page(page)

            # 将添加水印后的 PDF 保存到输出文件夹
            with open(output_pdf_path, "wb") as out_file:
                writer.write(out_file)

        print(f"为 {filename} 添加水印成功，保存为：{output_pdf_path}")

print("所有 PDF 文件处理完成！")
