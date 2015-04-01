import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./../img/human.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


plt.subplot(241), plt.imshow(img), plt.title('Original')
plt.xticks([]),  plt.yticks([])
plt.subplot(242), plt.imshow(erosion), plt.title('erosion')
plt.xticks([]),  plt.yticks([])
plt.subplot(243), plt.imshow(dilation), plt.title('deliation')
plt.xticks([]),  plt.yticks([])
plt.subplot(244), plt.imshow(opening), plt.title('opening')
plt.xticks([]),  plt.yticks([])
plt.subplot(245), plt.imshow(closing), plt.title('closing')
plt.xticks([]),  plt.yticks([])
plt.subplot(246), plt.imshow(gradient), plt.title('gradient')
plt.xticks([]),  plt.yticks([])
plt.subplot(247), plt.imshow(tophat), plt.title('tophat')
plt.xticks([]),  plt.yticks([])
plt.subplot(248), plt.imshow(blackhat), plt.title('blackhat')
plt.xticks([]),  plt.yticks([])

plt.tight_layout()
plt.show()
