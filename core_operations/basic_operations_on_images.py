# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt


img = cv2.imread(os.path.realpath('./../img/human.jpg'))


def item_access1():
    px = img[100, 100]
    print px
    img[100, 100] = [0, 0, 255]
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def item_access2():
    px = img[100, 100]
    print px
    img.itemset((100, 100, 0), 0)
    img.itemset((100, 100, 1), 0)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def image_roi_test():
    button = img[275: 285, 200: 210]
    button = img[200: 210, 275: 285]
    img[220: 230, 270: 280] = button
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def border_process():
    BLUE = [0, 0, 255]

    img1 = cv2.imread('./../img/opencv_logo.png')

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

    plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

    plt.show()


if __name__ == '__main__':
    #item_access1()
    #item_access2()
    #image_roi_test()
    border_process()
