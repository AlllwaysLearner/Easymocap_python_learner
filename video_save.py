import cv2


# 设置相机编号，0表示第一个相机，1表示第二个相机，以此类推
camera_ids = [0, 1, 2, 3]

# 设置视频文件保存路径
output_paths = [r"E:\\ACA-Dataset\\sanren\\0112.mp4",
                 r"E:\\ACA-Dataset\\sanren\\0212.mp4",
                r"E:\\ACA-Dataset\\sanren\\0312.mp4",
                 r"E:\\ACA-Dataset\\sanren\\0412.mp4"]
    # [r"E:\\ACA-Dataset\\wd\\01.mp4",
    #             r"E:\\ACA-Dataset\\wd\\02.mp4",
    #             r"E:\\ACA-Dataset\\wd\\03.mp4",
    #             r"E:\\ACA-Dataset\\wd\\04.mp4"]

#                [r"E:\\ACA-Dataset\\yxl\\01.mp4",
#                 r"E:\\ACA-Dataset\\yxl\\02.mp4",
#                 r"E:\\ACA-Dataset\\yxl\\03.mp4",
#                 r"E:\\ACA-Dataset\\yxl\\04.mp4"]

#                [r"E:\\ACA-Dataset\\yyx\\01.mp4",
#                 r"E:\\ACA-Dataset\\yyx\\02.mp4",
#                 r"E:\\ACA-Dataset\\yyx\\03.mp4",
#                 r"E:\\ACA-Dataset\\yyx\\04.mp4"]
# 设置视频捕捉对象列表
cap_list = [cv2.VideoCapture(cam_id) for cam_id in camera_ids]

# 获取视频的宽度和高度
width = int(cap_list[0].get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap_list[0].get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置视频写入对象列表
writer_list = [cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height)) for output_path in output_paths]

try:
    while True:
        for i, cap in enumerate(cap_list):
            ret, frame = cap.read()
            if not ret:
                print(f"Error reading frame from camera {i}")
                break

            # 在这里可以添加任何你需要的处理步骤，比如图像处理或分析

            # 保存视频帧
            writer_list[i].write(frame)

        # 检查按键输入
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == 27:  # ord('q')代表'q'字符的ASCII值，27是Esc键的ASCII值
            break


except KeyboardInterrupt:
    pass

finally:
    # 释放资源
    for cap in cap_list:
        cap.release()

    for writer in writer_list:
        writer.release()

    print("Video capture ended.")
