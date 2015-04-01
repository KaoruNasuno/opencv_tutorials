import cv2
import numpy as np
from matplotlib import pyplot as plt

def test():
    img = cv2.imread('./../img/human.jpg', 0)

    edges = cv2.Canny(img, 100, 200)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'),  plt.xticks([]),  plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'),  plt.xticks([]),  plt.yticks([])

    plt.tight_layout()
    plt.show()


def excercise():

    def nothing(x):
        pass

    img = cv2.imread('./../img/human.jpg', 0)
    cv2.namedWindow('image')

    l = 1000
    cv2.createTrackbar('max', 'image', 0, l, nothing)
    cv2.createTrackbar('min', 'image', 0, l, nothing)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        _max = cv2.getTrackbarPos('max', 'image')
        _min = cv2.getTrackbarPos('min', 'image')

        edges = cv2.Canny(img, _min, _max)
        jo = np.hstack((img, edges))
        cv2.imshow('image', jo)

if __name__ == '__main__':
    excercise()
