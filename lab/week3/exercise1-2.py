import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]

# Average Method
GrayScale = R/3 + G/3 + B/3

# Weight Method
GrayScale1 = 0.299*𝑅 + 0.587*𝐺 + 0.114*B


# End the GUI
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(GrayScale, cmap = 'gray')
#plt.imshow(GrayScale1, cmap = 'gray')
plt.show()

# Save image
filename = 'Ex2-gray.jpg'
cv2.imwrite(filename, GrayScale)