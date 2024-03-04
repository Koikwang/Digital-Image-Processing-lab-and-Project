import cv2
import numpy as np

# Load the image
image = cv2.imread('Ex6.jpg', cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection using Canny
edges = cv2.Canny(blurred, 50, 150)

# Detect lines using Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Draw detected lines on a copy of the image
line_image = image.copy()
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the image with detected lines
cv2.imshow('Hough Lines', line_image)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=20, param2=10, minRadius=0, maxRadius=0)

# Convert the (x, y) coordinates and radius of the circles to integers
#if circles is not None:
circles = np.uint16(np.around(circles))
circle_image = image.copy()
for circle in circles[0, :]:
    center = (circle[0], circle[1])
    radius = circle[2]
    # Draw the circle and its center
    cv2.circle(circle_image, center, radius, (0, 255, 0), 1)
    cv2.circle(circle_image, center, 1, (0, 0, 255), 1)

# Display the image with detected circles
cv2.imshow('Hough Circles', circle_image)

cv2.waitKey(0)
cv2.destroyAllWindows()