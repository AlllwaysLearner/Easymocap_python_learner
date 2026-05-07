这是一个完全免费开源的工具EasyMocap ，只用普通摄像头拍的视频，就能自动算出人体 3D 动作，还能生成任意角度的人物画面，不用贴标记点，小白也能上手玩！
用到的技术：
人体模型：SMPL / SMPL+H / SMPL-X / MANO
关键点检测：OpenPose、HRNet、MediaPipe
目标检测：YOLOv4
动作拟合：SPIN、VIBE、SMPLify-X
其中：
1.setup.py是 Python 项目的「安装配置文件」，用于把easymocap这个工具包安装到你的 Python 环境中，核心依赖setuptools库：
packages列表：指定要安装的子模块（比如数据集、3D 人体模型、标注工具等）；
entry_points：设置命令行快捷指令emc，执行这个指令就会运行apps.mocap.run里的main_entrypoint函数；
install_requires/data_files暂时为空，说明该包暂时无需额外依赖、无需安装额外数据文件。
2.video2frame.py 功能是把视频按指定频率提取成图片，还用到多线程加速处理多个视频：
核心函数video_to_frames：接收视频路径和输出文件夹，每 5 帧提取 1 张图片（frame_frequency=5），自动创建输出文件夹，用 OpenCV 读取视频并保存图片；
主程序部分：遍历指定文件夹下的所有视频，为每个视频开一个线程抽帧，避免单视频处理慢，最后打印处理进度。
3. 1camera.py用单个摄像头实时录制视频并保存为 MP4 文件：
cv2.VideoCapture(2)：打开编号为 2 的摄像头（0 是默认摄像头，1/2 是外接摄像头，可改）；
获取摄像头的宽高，设置视频编码器（mp4v 是 MP4 格式）；
创建视频写入对象，把摄像头实时读取的帧写入 MP4 文件；
显示摄像头画面，按q键停止录制，最后释放摄像头和文件资源。
4. draw3d.py读取 JSON 格式的 3D 人体关节点数据，用 matplotlib 画动态 3D 骨骼图：
核心函数visualize_keypoints：遍历指定文件夹的 JSON 文件，解析出 19 个 3D 关节点坐标；
用 3D 坐标系绘制关节点（红色圆点）和骨骼连线（蓝色线），每读一个 JSON 文件就画一帧，画完清空坐标系再画下一帧，实现「动态播放」效果；
预设了关节点的连接关系（比如鼻子连胸腔、左肩连左肘），并固定了坐标轴范围。
5. json2txt.py批量把文件夹里的 JSON 文件转换成 TXT 文件，本质是把 JSON 内容以格式化的方式写入 TXT：
核心函数json_to_txt：读取 JSON 文件内容，用json.dumps(indent=4)格式化（换行 + 缩进），再写入 TXT 文件；
主程序遍历指定文件夹，对每个 JSON 文件生成同名 TXT 文件。
6. video_save.py同时调用多个摄像头（最多示例里是 4 个），分别录制并保存成多个 MP4 文件：
camera_ids：摄像头编号列表（0/1/2/3 对应不同摄像头）；
output_paths：每个摄像头对应的视频保存路径；
用列表生成式创建多个摄像头捕捉对象和视频写入对象；
循环读取每个摄像头的帧，写入对应视频文件，按q或Esc停止，最后释放所有资源。