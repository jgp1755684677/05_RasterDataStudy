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


# Image segment
def image_segment(filename):
    # read the image
    image = cv2.imread(filename)
    mask = np.zeros(image.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rect = (0, 250, 2422, 1920)
    cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    image = image * mask2[:, :, np.newaxis]

    plt.imshow(image, cmap="gray")
    plt.colorbar()
    plt.show()


# watershed segment
def watershed_segment(filename):
    # read the image
    image = cv2.imread(filename)
    # transfer gray image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    # sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.2 * dist_transform.max(), 255, 0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]

    plt.imshow(image)
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
    # image_segment(image_filename)
    watershed_segment(image_filename)