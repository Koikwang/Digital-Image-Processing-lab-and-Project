# Import library
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the foreground image
foreground_image = cv2.imread('image/view.jpg')

# Read the background image
background_image = cv2.imread('image/Background-1.jpg')

# Convert the input image to HSV
hsv_image = cv2.cvtColor(foreground_image, cv2.COLOR_BGR2HSV)

# Define the lower and upper HSV thresholds for green
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Create a green mask
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Invert the mask
mask_inverse = cv2.bitwise_not(mask)

# Resize the background image to make the same size of the foreground image automatically
background_image = cv2.resize(background_image, (foreground_image.shape[1], foreground_image.shape[0]))

# Extract the foreground object using the mask from exercise 6-2, week 3 slide 33
foreground = cv2.bitwise_and(foreground_image, foreground_image, mask=mask_inverse)

# Extract the background using the mask from exercise 6-2, week 3 slide 33
background = cv2.bitwise_and(background_image, background_image, mask=mask)

# Combine foreground and background together
removal_image = foreground + background

# Convert color from BGR to RGB
image_rgb = cv2.cvtColor(removal_image, cv2.COLOR_BGR2RGB)

# Show image
plt.subplot(1, 5, 1)
plt.imshow(cv2.cvtColor(foreground_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 5, 2)
plt.imshow(cv2.cvtColor(mask_inverse, cv2.COLOR_BGR2RGB))
plt.title('Mask Inverse')
plt.axis('off')

plt.subplot(1, 5, 3)
plt.imshow(cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB))
plt.title('Foreground Mask')
plt.axis('off')

plt.subplot(1, 5, 4)
plt.imshow(cv2.cvtColor(background, cv2.COLOR_BGR2RGB))
plt.title('Background Mask')
plt.axis('off')

plt.subplot(1, 5, 5)
plt.imshow(image_rgb)
plt.title('Background Removal')
plt.axis('off')

plt.show()