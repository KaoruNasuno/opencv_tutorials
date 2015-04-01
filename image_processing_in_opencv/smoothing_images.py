import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./../img/human.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

filter2D = cv2.filter2D(img, -1, kernel)
averaging = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]),  plt.yticks([])
plt.subplot(232), plt.imshow(filter2D), plt.title('filter2D')
plt.xticks([]),  plt.yticks([])
plt.subplot(233), plt.imshow(averaging), plt.title('averaging')
plt.xticks([]),  plt.yticks([])
plt.subplot(234), plt.imshow(gaussian), plt.title('gaussian')
plt.xticks([]),  plt.yticks([])
plt.subplot(235), plt.imshow(median), plt.title('median')
plt.xticks([]),  plt.yticks([])
plt.subplot(236), plt.imshow(bilateral), plt.title('bilateral')
plt.xticks([]),  plt.yticks([])
plt.tight_layout()
plt.show()
