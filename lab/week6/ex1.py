import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Ex7.jpg')

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)

# Find contours
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create a copy of the original image to draw contours on
image_with_contours = image.copy()

# Loop through the contours and draw them
for contour in contours :
    area = cv2.contourArea(contour)
    print(area)
    if area > 30000 and area < 130000:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_with_contours, (x, y), (x + w, y + h), (0, 0, 255), 30)

# Convert the image to RGB format for displaying with matplotlib
image_rgb = cv2.cvtColor(image_with_contours, cv2.COLOR_BGR2RGB)

# Display the image with contours
plt.imshow(image_rgb)
plt.axis('off')
plt.show()
