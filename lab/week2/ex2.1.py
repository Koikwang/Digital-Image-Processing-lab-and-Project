import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

# Make pink square
img[1060:2400,1800:3200,0] = 147 #B
img[1060:2400,1800:3200,1] = 20  #G
img[1060:2400,1800:3200,2] = 255 #R

# Convert color
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.show()