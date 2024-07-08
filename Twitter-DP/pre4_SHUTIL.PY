import os
import shutil

# 读取.txt文件
txt_file_path = 'D://PyCharm/FS1/UP-MPF-main/datasets/twitter-dp/test-undp.txt'
with open(txt_file_path, 'r') as file:
    lines = file.readlines()

# 创建新文件夹用于存放复制后的图片
output_folder = 'D://PyCharm/FS1/UP-MPF-main/datasets/twitter-dp/image-undepressed'
os.makedirs(output_folder, exist_ok=True)

# 初始化新的图片序号
new_index = 151

# 循环处理每一行
for i, line in enumerate(lines):
    parts = line.split('\t')
    if len(parts) >= 3:
        index = parts[0]
        image_name = parts[2].strip()

        # 构建原始图片路径和目标图片路径
        source_path = f'D://PyCharm/FS1/UP-MPF-main/datasets/MVSA-S_data/{image_name}'
        target_name = f'{new_index}.jpg'
        target_path = os.path.join(output_folder, target_name)

        # 复制图片
        shutil.copy(source_path, target_path)

        # 更新.txt文件中的行
        lines[i] = line.replace(index, str(new_index))
        lines[i] = lines[i].replace(image_name, target_name)

        # 输出复制信息
        #print(f'Copied {source_path} to {target_path}')

        # 增加新的图片序号
        new_index += 1

# 更新.txt文件
with open(txt_file_path, 'w') as file:
    file.writelines(lines)


# 读取.tsv文件
# tsv_file_path = 'D://PyCharm/FS1/UP-MPF-main/datasets/twitter-dp/test-undp.txt'
# image_folder_path = 'D://PyCharm/FS1/UP-MPF-main/datasets/MVSA-S_data'
# output_folder_path = 'D://PyCharm/FS1/UP-MPF-main/datasets/twitter-dp/image-undp'

