# -*- coding: utf-8 -*-
import os
import cv2


# 获取工程根目录的路径
root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 输出工程根目录的路径
print("Root path: " + root_path)
# 获取数据文件的路径
data_path = os.path.abspath(root_path + r'\CVImage')
# 打印数据文件路径
print("Data path: " + data_path)
# 切换目录
os.chdir(data_path)
# 待处理图片文件名称
image_filename = "TestImage.png"
# 读取图片
image = cv2.imread(image_filename)
# 获取图片的高度和宽度
image_height, image_width = image.shape[0:2]
# 定义图片的显示的大小
image_size = (int(image_width * 0.5), int(image_height * 0.5))
# 缩放图片
image = cv2.resize(image, image_size, interpolation=cv2.INTER_AREA)
# BGR 转换成 HSV
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# 鼠标点击响应事件(获取HSV值)
def get_point_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("HSV is ", image_HSV[y, x])


# 鼠标点击响应事件(获取BGR值)
def get_point_bgr(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("BGR is ", image[y, x])


# 显示HSV格式图片
cv2.imshow("Image_HSV", image_HSV)
# 显示BGR格式图片
cv2.imshow("Image_BGR", image)
# 设置Image_HSV窗口鼠标点击回应事件
cv2.setMouseCallback("Image_HSV", get_point_hsv)
# 设置Image_BGR窗口鼠标点击回应事件
cv2.setMouseCallback("Image_BGR", get_point_bgr)
# 窗口暂停
cv2.waitKey(0)
