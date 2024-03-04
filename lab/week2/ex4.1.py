import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex3.jpg'
image = cv2.imread(image_path)
# Clone image
img = image.copy()

# Resized image
img_resized = cv2.resize(img, (480,270))

#cv2.INTER_NEAREST #nearest neighbor interpolation
#cv2.INTER_LINEAR #(default) bilinear interpolation
#cv2.INTER_CUBIC #bicubic interpolation
nearest_neighbor = cv2.resize(img, ( 200, 200 ), interpolation = cv2.INTER_NEAREST )

bilinear = cv2.resize(img, ( 200, 200 ), interpolation = cv2.INTER_LINEAR)

bicubic = cv2.resize(img, ( 200, 200 ), interpolation = cv2.INTER_CUBIC )

cv2.imshow('nearest_neighbor', nearest_neighbor)
cv2.imshow('bilinear', bilinear)
cv2.imshow('bicubic', bicubic)

# End the GUI
cv2.waitKey(0)
cv2.destroyAllWindows()