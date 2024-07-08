import os

folder_path = "D://PyCharm/FS1/UP-MPF-main/datasets/twittercopy" # 替换为你图片所在的文件夹路径

# 获取文件夹下所有文件
file_list = os.listdir(folder_path)

# 遍历文件列表
for filename in file_list:
    if filename.endswith(".jpg"):  # 确保只处理.jpg文件
        old_path = os.path.join(folder_path, filename)

        # 获取原始序号
        index = int(filename.split(".")[0])

        # 新的序号加上100
        new_index = index + 5862

        # 构造新的文件名
        new_filename = str(new_index) + ".jpg"

        new_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(old_path, new_path)

print("重命名完成。")
