# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

img_dir_path = os.path.realpath('./../img')

img = np.zeros((512, 512, 3), np.uint8)
drawing = False
mode = True
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

def test():
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


def draw_circle2(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDBLCLK:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        #if mode:
        #    cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        #else:
        #    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    ix, iy = x, y


def test2():
    global mode
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle2)
    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('m'):
            mode = not mode
        elif cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    #test()
    test2()
