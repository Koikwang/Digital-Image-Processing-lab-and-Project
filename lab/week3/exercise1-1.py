import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex1.jpg'
image = cv2.imread(image_path)
R = image[:,:,2]
G = image[:,:,1]
B = image[:,:,0]

# Average Method
GrayScale = R/3 + G/3 + B/3

# Weight Method
GrayScale1 = 0.299*𝑅 + 0.587*𝐺 + 0.114*B

# Calculate binary image
threshold_value = 128 
binary = GrayScale > threshold_value

# End the GUI
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(GrayScale, cmap = 'gray')
#plt.imshow(GrayScale1, cmap = 'gray')
plt.imshow(binary, cmap = 'gray')
plt.show()