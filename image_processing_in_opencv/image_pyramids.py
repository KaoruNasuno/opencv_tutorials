import cv2
import numpy as np
from matplotlib import pyplot as plt


def test():
    img = cv2.imread('./../img/human.jpg')

    lower_reso = cv2.pyrDown(img)
    cv2.imshow('image', lower_reso)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()
