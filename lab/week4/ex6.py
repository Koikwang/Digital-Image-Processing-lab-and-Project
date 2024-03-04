import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('ex6.jpg')

# Clone image
img = image.copy()

kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

img_filtered = cv2.filter2D(img, -1, kernel)
image_rgb = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2RGB)

filter_sepia = np.array([[0.272, 0.534, 0.131],
                         [0.349, 0.686, 0.168],
                         [0.393, 0.769, 0.189]])
# Applying cv2.transform function
sepia_img = cv2.transform(img, filter_sepia)
image_rgb1 = cv2.cvtColor(sepia_img, cv2.COLOR_BGR2RGB)

filter_emboss = np.array([[3, -2, -3],
                          [-4, 8, -6],
                          [5, -1, 0]])
# Applying cv2.filter2D function
edge_detection = cv2.filter2D(img, -1, filter_emboss)
image_rgb2 = cv2.cvtColor(edge_detection, cv2.COLOR_BGR2RGB)

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('img_filtered')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(image_rgb1)
plt.title('sepia_img')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(image_rgb2)
plt.title('edge_detection')
plt.axis('off')

plt.show()
