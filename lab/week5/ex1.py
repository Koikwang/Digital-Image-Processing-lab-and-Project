import numpy as np
import cv2

# Define the source and destination points
src_points = np.float32([[50, 50], [200, 50], [50, 200]])
dst_points = np.float32([[70, 100], [200, 100], [100, 250]])

# Calculate the affine transformation matrix
M = cv2.getAffineTransform(src_points, dst_points)

# Print the transformation matrix
print("Transformation Matrix (M):")
print(M)