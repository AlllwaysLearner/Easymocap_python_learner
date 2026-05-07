import cv2

# 打开默认摄像头
cap = cv2.VideoCapture(2)
# 获取视频的宽度和高
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置视频编码器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# 创建视频输出对象
out = cv2.VideoWriter(r'E:\ACA-Dataset\chessboard\intri\04.mp4', fourcc, 30.0, (width, height))

# 创建一个窗口
cv2.namedWindow("Captured Video")

while True:
    # 读取一帧视频
    ret, frame = cap.read()

    # 将帧写入视频文件
    out.write(frame)

    # 显示当前帧
    cv2.imshow("Captured Video", frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()