import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_logarithmic(img):
    img = img.astype(np.double)
    adjusted_logarithmic = np.clip(((255 * (np.log(1+img))) / (np.log(1+vmax))), 0, 255).astype(np.uint8)
    return adjusted_logarithmic

# Read image
image_path = 'Ex2-2.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Clone image
img = image.copy()

vmax = np.max(img)

# Adjust logarithmic
adjusted_logarithmic_image = adjust_logarithmic(img)
plt.imshow(adjusted_logarithmic_image, cmap='gray')
plt.title('Adjusted logarithmic')
plt.show()
