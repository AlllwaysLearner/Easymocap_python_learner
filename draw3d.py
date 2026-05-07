import os
import json
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

def visualize_keypoints(folder_path, connections):
    # 创建一个坐标系
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 遍历文件夹内的文件
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.json'):
            json_file = os.path.join(folder_path, filename)

            try:
                with open(json_file, 'r') as file:
                    json_data = json.load(file)

                    keypoints = json_data[0]['keypoints3d'][:19]

                    # 提取每个关节点的坐标
                    x = [keypoint[0] for keypoint in keypoints]
                    y = [keypoint[1] for keypoint in keypoints]
                    z = [keypoint[2] for keypoint in keypoints]

                    # 绘制关节点
                    ax.scatter(x, y, z, marker='o', color='r')

                    # 绘制关节点之间的连线
                    for i, connection in enumerate(connections):
                        start_index, end_index = connection
                        ax.plot([x[start_index], x[end_index]], [y[start_index], y[end_index]],
                                [z[start_index], z[end_index]], color='b')

                    # 设置坐标轴标签
                    ax.set_xlabel('X')
                    ax.set_ylabel('Y')
                    ax.set_zlabel('Z')

                    # 设置坐标轴范围
                    ax.set_xlim3d(-0.7, 1.1)
                    ax.set_ylim3d(-0.7, 1.1)
                    ax.set_zlim3d(0, 2)

                    # 显示图形
                    plt.draw()
                    plt.pause(0.01)  # 控制每帧之间的时间间隔
                    ax.cla()  # 清空坐标系，准备绘制下一帧

            except json.JSONDecodeError:
                print(f"Error reading JSON file: {json_file}")
                continue
            except (KeyError, IndexError):
                print(f"Invalid JSON data in file: {json_file}")
                continue

# 关节点索引
keypoints_indices = ['鼻子', '胸腔', '左肩', '左肘', '左手', '右肩', '右肘', '右手', '髋', '左髋', '左膝', '左脚', '右髋', '右膝', '右脚', '左眼',
                     '右眼', '左耳', '右耳']

# 关节点之间的连接关系，以索引形式表示
connections = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7), (1, 8), (8, 9),
               (9, 10), (10, 11), (8, 12), (12, 13), (13, 14), (0, 15), (0, 16), (15, 17),
               (16, 18)]

# 文件夹路径
folder_path = r"C:\Users\WangDing\Desktop\dacne_9view_output\keypoints3d"
#r"C:\Users\WangDing\Desktop\output\keypoints3d"
# 可视化关节点坐标
visualize_keypoints(folder_path, connections)