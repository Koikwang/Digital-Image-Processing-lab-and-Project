import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

# Calculate the inverse image
inverse_image = 255 - img

# Convert color
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image_rgb1 = cv2.cvtColor(inverse_image, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_rgb1)
plt.title('Inverse Image')
plt.axis('off')

plt.tight_layout()
plt.show()
