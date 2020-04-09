import os
import cv2
import time


def trend_line_extract(filename, template, Min, Max):
    # read the file by gray.
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    # Gaussian blur is applied to the image.
    image_gauss = cv2.GaussianBlur(image, (template, template), 0)
    # canny edge detection.
    image_canny = cv2.Canny(image_gauss, Min, Max)
    # define the name of export image.
    out_filename = filename + '(Gauss_{0}_Min{1}_Max{2}.tif)'.format(template, Min, Max)
    # write data to file.
    cv2.imwrite(out_filename, image_canny)
    # show the image.
    cv2.imshow(filename, image)
    # show the Gaussian blur image.
    cv2.imshow('Image Gaussian', image_gauss)
    # show the result.
    cv2.imshow(out_filename, image_canny)
    # the window waiting.
    cv2.waitKey(0)


if __name__ == '__main__':
    # get path of the project.
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # export project path.
    print("Root path:" + root_path)
    # define the path of data.
    data_path = os.path.abspath(root_path + r"\CVImage")
    # export data path.
    print("Data path:" + data_path)
    # change the path.
    os.chdir(data_path)
    # dem filename.
    dem_filename = 'dem.tif'
    # call the function.
    trend_line_extract(dem_filename, 5, 1, 7)
