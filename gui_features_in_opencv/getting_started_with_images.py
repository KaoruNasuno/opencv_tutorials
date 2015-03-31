# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

img_dir_path = os.path.realpath('./../img')


def test():
    img = cv2.imread(img_dir_path + '/messi.jpg', 0)
    cv2.imshow('image', img)

    k = cv2.waitKey(0) & 0xFF
    # case statement below seems not working correctly
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite(img_dir_path + '/messigray.png', img)
        cv2.destroyAllWindows()


def test2():
    img = cv2.imread(img_dir_path + '/messi.jpg', 0)
    print img
    print type(img)
    print img.shape
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    #test()
    test2()
