# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# 图片基本信息获取及不同效果显示
def cv_image_show(filename):
    # 利用cv2读取图像
    image = cv2.imread(filename)
    # 输出图像的高度、宽度、通道数
    print(image.shape)
    # 输出图像大小
    print(image.size)
    # 输出图像的位数
    print(image.dtype)
    # 输出图片像素的均值
    print(cv2.mean(image))
    # 渲染图像
    cv2.imshow("MyHome", image)
    # 分离RGB通道
    image_b, image_g, image_r = cv2.split(image)
    # 渲染图像的R通道
    cv2.imshow("MyHome_B", image_b)
    # 渲染图像的G通道
    cv2.imshow("MyHome_G", image_g)
    # 渲染图像的B通道
    cv2.imshow("MyHome_R", image_r)
    # 获得灰度图像
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 获取二值化图像
    ret, image_binary = cv2.threshold(image_grey, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # 渲染二值化图像
    cv2.imshow("MyHome Binary Image", image_binary)
    # 窗口停止
    cv2.waitKey(0)
    # 关闭所有的窗口
    cv2.destroyAllWindows()


# 设置字体格式为SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置字体格式为Times New Roman
plt.rcParams['font.sans-serif'] = ['Times New Roman']
# 显示坐标轴符号
plt.rcParams['axes.unicode_minus'] = False
# 设置分辨率
plt.rcParams['figure.dpi'] = 100


# 获取RGB三个通道的直方图并绘制到一张图里
def get_rgb_hist(filename):
    # 读取图片
    image_bgr = cv2.imread(filename, cv2.IMREAD_COLOR)
    # 获取图片的B通道
    image_b = image_bgr[..., 0]
    # 获取图片的G通道
    image_g = image_bgr[..., 1]
    # 获取图片的R通道
    image_r = image_bgr[..., 2]
    # 分通道显示图片
    figure = plt.gcf()
    # 设置窗口的大小
    figure.set_size_inches(10, 15)
    # 设置分为两行三列，第一行合并
    plt.subplot(321)
    # 将图片转换成数组显示
    plt.imshow(np.flip(image_bgr, axis=2))
    # 不显示坐标轴
    plt.axis('off')
    # 设置图片的标题
    plt.title("MyHome")

    # R通道图片显示位置
    plt.subplot(322)
    # 以灰度图形式显示R通道
    plt.imshow(image_r, cmap="gray")
    # 不显示坐标轴
    plt.axis('off')
    # 设置图片的标题
    plt.title('MyHome_R')

    # G通道图片显示位置
    plt.subplot(323)
    # 以灰度图形式显示R通道
    plt.imshow(image_g, cmap="gray")
    # 不显示坐标轴
    plt.axis('off')
    # 设置图片的标题
    plt.title('MyHome_G')

    # B通道图片显示位置
    plt.subplot(324)
    # 以灰度图形式显示R通道
    plt.imshow(image_b, cmap="gray")
    # 不显示坐标轴
    plt.axis('off')
    # 设置图片的标题
    plt.title('MyHome_B')

    # 按 R、G、B 三个通道分别计算颜色直方图
    b_hist = cv2.calcHist([image_bgr], [0], None, [256], [0, 256])
    g_hist = cv2.calcHist([image_bgr], [1], None, [256], [0, 256])
    r_hist = cv2.calcHist([image_bgr], [2], None, [256], [0, 256])

    # 设置窗口
    plt.subplot(313)
    # 显示三个通道的颜色直方图
    plt.plot(b_hist, label='B', color="blue")
    plt.plot(g_hist, label='G', color="green")
    plt.plot(r_hist, label='R', color="red")
    plt.legend(loc='best')
    plt.xlim([0, 256])
    plt.show()


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
    # cv_image_show(image_filename)
    # 调用函数
    get_rgb_hist(image_filename)
