import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Ex2-noise.jpg')

# Clone image
img = image.copy()

# Apply bilateral filter
filtered_image = cv2.bilateralFilter(img, d=159, sigmaColor=1, sigmaSpace=1)

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Sobel X-direction')
plt.axis('off')

cv2.waitKey(0)
cv2.destroyAllWindows()


