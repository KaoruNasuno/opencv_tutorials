# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt


def test1():
    x = np.uint8([250])
    y = np.uint8([10])
    print cv2.add(x, y)
    print x, y


def test2():
    img1 = cv2.imread(os.path.realpath('./../img/human.jpg'))
    img2 = cv2.imread(os.path.realpath('./../img/opencv_logo.png'))

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    rows, cols, channels = img2.shape
    roi = img1[0: rows, 0: cols]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    cv2.imshow('img2gray', img2gray)
    cv2.imshow('mask', mask)
    cv2.imshow('mask_inv', mask_inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    cv2.imshow('img1_bg', img1_bg)
    cv2.imshow('img2_fg', img2_fg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    dst = cv2.add(img1_bg, img2_fg)
    img1[0: rows, 0: cols] = dst

    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test2()
