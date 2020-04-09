# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# set the Chinese font to SimHei.
plt.rcParams['font.sans-serif'] = ['SimHei']
# set the English font to Times New Roman.
plt.rcParams['font.sans-serif'] = ['Times New Roman']
# not show the axes less than zero.
plt.rcParams['axes.unicode_minus'] = False
# set resolution to 100
plt.rcParams['figure.dpi'] = 100


# extract image contour
def cv_find_contours(filename):
    # read the image.
    image = cv2.imread(filename)
    # resize the image.
    image = cv2.resize(image, None, fx=0.7, fy=0.7)
    # get current figure.
    fig = plt.gcf()
    # set the window size.
    fig.set_size_inches(10, 15)
    # set current image location.
    plt.subplot(221)
    # transfer image from BGR to RGB and show the image.
    plt.imshow(np.flip(image, axis=2))
    # not show the axes less than zero.
    plt.axis('off')
    # set the image tile
    plt.title('Image')

    # 定义掩膜值
    bgr = np.array([82, 76, 46])
    # 最大掩膜值
    bgr_upper = bgr + 10
    # 最小掩膜值
    bgr_lower = bgr - 10
    # 获取淹没区域
    image_mask = cv2.inRange(image, bgr_lower, bgr_upper)
    # 定义图片的位置
    plt.subplot(222)
    # 显示提取的边缘
    plt.imshow(image_mask, cmap='gray')
    # 不显示坐标轴
    plt.axis('off')
    # 设置标题
    plt.title('Mask')

    # 使用 cv2.findContours()函数对 mask 图片提取轮廓，并调用 cv2.drawContour()把轮廓 叠加在原始图像
    contours, hicrarchy = cv2.findContours(image_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 输出边缘个数
    print("number of contours:%d" % (len(contours)))
    # 复制图片
    all_lakes_image = image.copy()
    # 绘制图片
    cv2.drawContours(all_lakes_image, contours, -1, (0, 0, 255), 2)
    # 定义图片的位置
    plt.subplot(223)
    # 显示图片
    plt.imshow(all_lakes_image)
    # 设置坐标轴不显示
    plt.axis('off')
    # 设置图片的标题
    plt.title('All Contours')

    # 复制图片
    the_largest_lake = image.copy()
    # 按轮廓长度排序
    contours.sort(key=len, reverse=True)
    # 绘制长度最长的轮廓
    cv2.drawContours(the_largest_lake, [contours[0]], -1, (0, 0, 255), 2)
    # 定义图片的位置
    plt.subplot(224)
    # 显示图片
    plt.imshow(the_largest_lake)
    # 不显示坐标轴
    plt.axis('off')
    # 设置图片的标题
    plt.title('Big Contours')
    # 显示
    plt.show()


def canny_edge(filename):
    # 读取图片的B通道
    image = cv2.imread(filename, 0)
    # 高斯平滑降噪
    image = cv2.GaussianBlur(image, (3, 3), 0)
    # 显示高斯平滑结果
    cv2.imshow('GaussianBlur', image)
    # canny提取轮廓
    canny = cv2.Canny(image, 0, 45)
    # 显示提取的轮廓值
    cv2.imshow('MyHome_Canny', canny)
    # 窗口停止
    cv2.waitKey(0)
    # 关闭所有窗口
    cv2.destroyAllWindows()


def sobel_edge(filename):
    image = cv2.imread(filename, 0)
    # 获取图片的高度和宽度
    image_height, image_width = image.shape[0:2]
    # 定义图片的显示的大小
    image_size = (int(image_width * 0.5), int(image_height * 0.5))
    # 缩放图片
    image = cv2.resize(image, image_size, interpolation=cv2.INTER_AREA)
    x = cv2.Sobel(image, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(image, cv2.CV_16S, 0, 1)
    Scale_absX = cv2.convertScaleAbs(x)
    Scale_absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
    cv2.imshow('img', image)
    cv2.imshow('Scale_absX', Scale_absX)
    cv2.imshow('Scale_absY', Scale_absY)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def laplacian_edge(filename):
    img = cv2.imread(filename, 0)
    laplacian = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
    dst = cv2.convertScaleAbs(laplacian)
    cv2.imshow('Laplacian', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    # 获取工程根目录的路径
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 打印工程根目录路径
    print("Root path:" + root_path)
    # 定义数据文件的路径
    data_path = os.path.abspath(root_path + r"\CVImage")
    # 打印数据文件的路径
    print("Data path:" + data_path)
    # 切换目录
    os.chdir(data_path)
    # 待操作的图片文件名
    image_filename = "TestImage.png"
    # 调用函数
    # cv_find_contours(image_filename)
    # canny_edge(image_filename)
    # sobel_edge(image_filename)
    laplacian_edge(image_filename)
