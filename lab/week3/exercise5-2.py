import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

min_intensity = 0
max_intensity = 255

img = img.astype(np.double)

# Creating Histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

stretched_image = ((255 * (img - min_intensity)) / (max_intensity - min_intensity))

# Ensure pixel values are within [0, 255] range
stretched_image = np.clip(stretched_image, 0, 255)

# Convert stretched image back to uint8
stretched_image = stretched_image.astype(np.uint8)

# Calculate histogram of stretched image
hist_stretched = cv2.calcHist([stretched_image], [0], None, [256], [0, 256])

im = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Histogram Equalization
hist_eq = cv2.equalizeHist(im)
hist_equalized = cv2.calcHist([hist_eq], [0], None, [256], [0, 256])

plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Pixel')
plt.show()

plt.plot(hist_stretched, color='b')
plt.title('Stretched Histogram')
plt.xlabel('')
plt.ylabel('')
plt.show()

plt.plot(hist_equalized, color='b')
plt.title('Equalization Histogram')
plt.xlabel('')
plt.ylabel('')
plt.show()
