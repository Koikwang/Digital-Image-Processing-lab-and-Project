import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
img = cv.imread('/content/drive/MyDrive/dataset/ITCS518/12.jpg', cv.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
erode_img = cv.erode(img, kernel)
fig=plt.figure()
#fig.add_subplot(rows, columns, i)
fig.add_subplot(1,2,1)
plt.imshow(img, cmap='gray')
fig.add_subplot(1,2,2)
plt.imshow(erode_img, cmap='gray')
plt.show()