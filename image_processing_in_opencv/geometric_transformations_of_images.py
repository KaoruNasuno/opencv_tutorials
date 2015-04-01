# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

img = cv2.imread('./../img/human.jpg')


def test_scaling():
    cv2.imshow('org', img)
    res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('pattern1', res)

    height, width = img.shape[:2]
    res = cv2.resize(img, (int(0.5 * width), int(0.5 * height)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('pattern2', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_translation():
    rows, cols, _ = img.shape
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_rotation():
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_affine_transformation():
    rows, cols, _ = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('org', img)
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_perspective_transformation():
    global img
    rows, cols, _ = img.shape
    # [x, y]
    a = [253, 38]
    b = [250, 115]
    #b = [250, 80]
    c = [318, 35]
    d = [310, 115]
    pts1 = np.float32([a, b, c, d])
    #pts1 = np.float32([a, c, b, d])
    #pts1 = np.float32([[38, 253], [115, 250], [35, 318], [115, 310]])
    pts2 = np.float32([[0, 0], [0, 150], [200, 0], [200, 150]])
    #pts2 = np.float32([[0, 0], [200, 0], [0, 150], [200, 150]])
    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (150, 200))
    a.reverse()
    b.reverse()
    c.reverse()
    d.reverse()
    img[a[0], a[1]] = [0, 0, 255]
    img[b[0], b[1]] = [0, 0, 255]
    img[c[0], c[1]] = [0, 0, 255]
    img[d[0], d[1]] = [0, 0, 255]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


if __name__ == '__main__':
    #test_scaling()
    #test_translation()
    #test_rotation()
    #test_affine_transformation()
    test_perspective_transformation()
