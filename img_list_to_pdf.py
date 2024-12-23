from PIL import Image


def images_to_pdf(image_paths, output_pdf_path):
    """
    将多张图片合成为一个 PDF 文件。

    :param image_paths: 图片文件路径的列表（按顺序排列）。
    :param output_pdf_path: 输出 PDF 文件的路径。
    """
    # 打开第一张图片作为 PDF 的初始页
    image_list = []
    for image_path in image_paths:
        img = Image.open(image_path).convert("RGB")  # 确保图片是 RGB 模式
        image_list.append(img)

    # 保存到 PDF
    if image_list:
        first_image = image_list[0]
        first_image.save(output_pdf_path, save_all=True, append_images=image_list[1:])


# 示例使用
image_paths = ["image1.jpg", "image2.png", "image3.jpeg"]  # 替换为你的图片路径
output_pdf_path = "output.pdf"  # 输出 PDF 文件名
images_to_pdf(image_paths, output_pdf_path)
print(f"PDF 已保存到: {output_pdf_path}")
