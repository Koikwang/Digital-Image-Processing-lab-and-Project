import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('Ex2-gray.jpg')

# Clone image
img = image.copy()

kernel_size = 5

height = img.shape
width = img.shape

filtered_image = np.zeros_like(img)
#print(filtered_image)
radius = kernel_size // 2

# Apply the mean filter using nested loops
for y in range(radius, height - radius):
    for x in range(radius, width - radius):
        


plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.imshow(filtered_image, cmap='gray')
plt.title('Mean Filtered Image')
plt.show()
