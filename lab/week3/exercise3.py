import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(img, beta):
    img = img.astype(np.double)
    adjusted_brightness = np.clip(img + beta, 0, 255).astype(np.uint8)
    return adjusted_brightness

def adjust_contrast(img, alpha):
    adjusted_contrast = np.clip(alpha * img, 0, 255).astype(np.uint8)
    return adjusted_contrast

# Read image
image_path = 'Ex2-gray.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

alpha = 1.5
beta = 128

# Adjust brightness
adjusted_brightness_image = adjust_brightness(img, beta)
plt.imshow(adjusted_brightness_image)
plt.title('Adjusted Brightness')
plt.show()

# Adjust contrast
adjusted_contrast_image = adjust_contrast(img, alpha)
plt.imshow(adjusted_contrast_image)
plt.title('Adjusted Contrast')
plt.show()
