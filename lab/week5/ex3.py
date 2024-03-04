import cv2
import numpy as np

# Load the image
image = cv2.imread('Ex5.jpg', cv2.IMREAD_GRAYSCALE)

# Clone the image for visualization
img = image.copy()

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# Filter by Area.
params.filterByArea = True
params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

# Define a function to classify blobs as triangles
def classify_triangle(blob):
    if len(blob) == 3:
        return True
    return False

# Detect and print triangles
triangle_count = 0
for keypoint in keypoints:
    x, y = int(keypoint.pt[0]), int(keypoint.pt[1])
    size = keypoint.size
    roi = image[y - int(size / 2):y + int(size / 2), x - int(size / 2):x + int(size / 2)]
    if classify_triangle(roi):
        triangle_count += 1
        print(f"Triangle {triangle_count}: ({x}, {y})")

# Draw detected blobs as green circles on the image
result_image = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image with detected objects
cv2.imshow('Detected Objects', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
