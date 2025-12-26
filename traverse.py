import os

# 目标文件夹路径（请修改为你的实际路径）
folder_path = r"F:\OCTA2024\oct2octa\octa"

# 生成预期的文件编号集合（10000 ~ 10845）
expected_nums = set(range(10000, 10846))

# 遍历文件夹，获取已存在的npy文件编号
existing_nums = set()
for filename in os.listdir(folder_path):
    if filename.endswith('.npy'):
        file_num = int(filename.split('.')[0])
        existing_nums.add(file_num)

# 找出缺失的编号并拼接为文件名
missing_num = (expected_nums - existing_nums).pop()
missing_filename = f"{missing_num}.npy"

# 输出缺失的文件名
print(f"缺失的文件：{missing_filename}")