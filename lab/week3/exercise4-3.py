import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_exponential(img, vmax, k):
    img = img.astype(np.double)
    adjusted_exponential = np.clip((255 * ((np.power(k, img)) - 1)) / ((np.power(k, vmax)) - 1), 0, 255).astype(np.uint8)
    return adjusted_exponential

# Read image
image_path = 'Ex2-3.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

vmax = np.max(img)
k = 1.5

# Adjust exponential
adjusted_exponential_image = adjust_exponential(img, vmax, k)
plt.imshow(adjusted_exponential_image, cmap='gray')
plt.title('Adjusted exponential')
plt.show()
