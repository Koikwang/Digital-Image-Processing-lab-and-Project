import cv2
import numpy as np

image = cv2.imread('Ex2-gray.jpg')

# Clone image
img = image.copy()

filtered_image = cv2.medianBlur(img, 50)

smaller_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
smaller_filtered_image = cv2.resize(filtered_image, (filtered_image.shape[1] // 2, filtered_image.shape[0] // 2))

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save image
filename = 'output-ex3-test.jpg'
cv2.imwrite(filename, filtered_image)