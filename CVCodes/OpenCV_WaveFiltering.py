import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 设置文字的格式为SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置文字的格式为Times New Roman
plt.rcParams['font.sans-serif'] = ['Times New Roman']
# 显示负坐标轴
plt.rcParams['axes.unicode_minus'] = False
# 设置分辨率
plt.rcParams['figure.dpi'] = 100


def filtering(filename):
    # read the image
    image = cv2.imread(filename)
    # flip the array by 2
    image_flip = np.flip(image, axis=2)
    # mean filtering
    image_mean = cv2.blur(image, (5, 5))
    # Guassian filtering
    image_guassian = cv2.GaussianBlur(image, (5, 5), 0)
    # median filtering
    image_median = cv2.medianBlur(image, 5)
    # bilateral filtering
    image_bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    # define image titles
    image_titles = ['Image', 'Image_Mean', 'Image_Gaussian', 'Image_Median', 'Image_Bilateral']
    # define image to show
    images = [image_flip, image_mean, image_guassian, image_median, image_bilateral]
    # show the image
    for i in range(5):
        # define the position of image.
        plt.subplot(2, 3, i+1)
        # render the image
        plt.imshow(images[i])
        # setting the title of image.
        plt.title(image_titles[i])
    # show
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
    image_filename = "YellowPeaches.jpg"
    # use the function.
    filtering(image_filename)