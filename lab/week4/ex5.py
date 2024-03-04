import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Ex3.jpg')

# Clone image
img = image.copy()

# Sobel operation in X-direction
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
abs_sobelx = cv2.convertScaleAbs(sobel_x)

# Sobel operation in Y-direction
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
abs_sobely = cv2.convertScaleAbs(sobel_y)

# Laplacian operation
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
abs_laplacian = cv2.convertScaleAbs(laplacian)

# Canny edge detection
edges = cv2.Canny(img, threshold1=100, threshold2=200)

# Display using Matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(abs_sobelx, cv2.COLOR_BGR2RGB))
plt.title('Sobel X-direction')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(abs_sobely, cv2.COLOR_BGR2RGB))
plt.title('Sobel Y-direction')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(abs_laplacian, cv2.COLOR_BGR2RGB))
plt.title('Laplacian')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

plt.tight_layout()
plt.show()
