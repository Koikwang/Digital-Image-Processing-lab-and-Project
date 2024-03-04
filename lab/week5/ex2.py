import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Ex2-perspective.jpg')

# Clone image
img = image.copy()

# Define the source points (4 corners of a region of interest)
src_points = np.float32([[115,60], [183, 85], [124, 189], [197, 192]])
## Define the destination points (corresponding 4 corners in the output image)

dst_points = np.float32([[0,0], [200,0], [0, 190], [195, 192]])

# Compute the perspective transform matrix
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply the perspective transform to the image
output_image = cv2.warpPerspective(img, perspective_matrix, (195, 190))

image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

#plt.imshow(image)
plt.imshow(image_rgb)
#plt.axis('off')

plt.show()
