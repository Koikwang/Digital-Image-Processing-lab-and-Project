import cv2

# Read images
image1 = cv2.imread('Ex4.jpg')
image2 = cv2.imread('Ex2.jpg')

# Make images have the same dimensions
image2 = cv2.resize(image2, image1.shape[1::-1])

alpha = 0.5

result = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)

cv2.imshow('Alpha Blending Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
