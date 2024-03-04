import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image/money_all.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# No longer use
def avg_circle_value_legacy(img, circle):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b, g, r = [], [], []
    for y, _ in enumerate(gray):
        for x, _ in enumerate(img[y]):
            dx = x - circle[0]
            dy = y - circle[1]
            distance_squared = dx ** 2 + dy ** 2
            if distance_squared <= np.power(circle[2], 2):
                b.append(img[y, x, 0])
                g.append(img[y, x, 1])
                r.append(img[y, x, 2])
    return np.average(b).astype(np.uint8), np.average(g).astype(np.uint8), np.average(r).astype(np.uint8)

def avg_circle_value(img, circle):
    center_x, center_y, radius = circle

    y, x = np.ogrid[:img.shape[0], :img.shape[1]]
    mask = (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2

    b = img[:, :, 0][mask]
    g = img[:, :, 1][mask]
    r = img[:, :, 2][mask]

    avg_b = np.average(b).astype(np.uint8)
    avg_g = np.average(g).astype(np.uint8)
    avg_r = np.average(r).astype(np.uint8)

    return avg_b, avg_g, avg_r

def get_coin_value(r, g, b):
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    
    if b > 180 and g > 180 and r > 180:
        return 1
    if b < 50 and g < 50 and r < 50:
        return 50
    elif max_val > min_val + 50:
        if max_val == r:
            return 5
        if max_val == g:
            return 10
        if max_val == b:
            return 20
    else:
        return 100
    
# count coin
# Adjust for every image: param1, param2, minRadius, maxRadius
circles = cv2.HoughCircles(
    gray,  # Input image (grayscale)
    cv2.HOUGH_GRADIENT,  # Detection method (Hough Gradient)
    dp=1,  # Inverse ratio of accumulator resolution to image resolution
    minDist=35,  # Minimum distance between detected circles
    param1=20,  # Upper threshold for edge detection
    param2=50,  # Threshold for circle center detection
    minRadius=30,  # Minimum radius of detected circles
    maxRadius=52   # Maximum radius of detected circles (0 for unlimited)
)

counter = 0
result_image = image.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        # Drawing a green circle of each detected coin
        center = (circle[0], circle[1])  # Circle center coordinates
        radius = circle[2]  # Circle radius
        cv2.circle(result_image, center, radius, (0, 255, 0), 10)  # Draw the circle
        
        b, g, r = avg_circle_value(image, circle)
        
        counter += get_coin_value(r,g,b)
        print(r,g,b, counter)
        
print("Coin counted: ", counter)

img = image.copy()

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
pre = cv2.medianBlur(img, 5)

for i in range(0, 10):
    pre = cv2.morphologyEx(pre, cv2.MORPH_ERODE, kernel)
pre = cv2.medianBlur(pre, 3)

# Find Canny edges
edged = cv2.Canny(pre, 120, 240)

for i in range(0, 10):
    edged = cv2.morphologyEx(edged, cv2.MORPH_DILATE, kernel)
    edged = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    
gradient = cv2.morphologyEx(edged, cv2.MORPH_GRADIENT, kernel)
display_image = cv2.cvtColor(gradient, cv2.COLOR_BGR2RGB)

new_edged = edged.copy()
contours, hierarchy = cv2.findContours(new_edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    if (w > 200 and w < 300) and (h > 300 and h < 510):
        w = w//2
        h = h//2
        # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        img = cv2.rectangle(img, (x+(w//2), y+(h//2)), (x + w + w//2, y + h + h//4), (0, 255, 0), 10)
        # print(w, h)
        # print(f"Area: {(x+(w//2), y+(h//2))} to {(x + w, y + h)}")

        # Define the ROI (Region of Interest)
        roi = img[(y+(h//2)):y+h, (x+(w//2)):x+w]
        # Calculate the average color within the ROI
        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        # Calculate the average color within the ROI
        avg_color = np.mean(roi_rgb, axis=(0, 1))  # Calculate mean across all channels (RGB)
        # Convert average color to integers
        avg_color = avg_color.astype(int)
        h = avg_color[0]
        s = avg_color[1]
        v = avg_color[2]
        
        if h >= 41 and h <= 50:
            counter += 20 # Bank: 20
        elif h >= 51 and h <= 60:
            counter += 100 # Bank: 100
        elif h >= 71 and h <= 80:
            counter += 500 # Bank: 500
        elif h >= 100 and h <= 110:
            counter += 50 # Bank: 50
        elif h >= 111 and h <= 120:
            counter += 1000 # Bank: 1000
        else:
            counter += 0

        print(f"Area: {(x+(w//2), y+(h//2))} to {(x + w, y + h)} Center: ({x}, {y}), Average Color: {avg_color}")
    
print("Bank + Coin counted", counter)
# Draw the contours on the original image
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Show image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.title('Coin Detection')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_HSV2BGR),cv2.COLOR_BGR2RGB))
plt.title('Bank note detection')
plt.axis('off')

plt.show()