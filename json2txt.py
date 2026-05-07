import os
import json

def json_to_txt(json_file, txt_file):
    with open(json_file, 'r') as json_file:
        json_data = json.load(json_file)

    with open(txt_file, 'w') as txt_file:
        txt_file.write(json.dumps(json_data, indent=4))

# 指定文件夹路径
folder_path = r"C:\Users\WangDing\Desktop\keypoints3d"

# 遍历文件夹内的文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        json_file = os.path.join(folder_path, filename)
        txt_file = os.path.join(folder_path, f'{os.path.splitext(filename)[0]}.txt')
        json_to_txt(json_file, txt_file)