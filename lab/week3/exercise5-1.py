import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Creating Histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist1 = cv2.calcHist([image], [1], None, [256], [0, 256])
hist2 = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(hist)
plt.plot(hist1)
plt.plot(hist2)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Pixel')
plt.show()
