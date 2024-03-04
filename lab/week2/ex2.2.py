import cv2
import matplotlib.pyplot as plt 

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Clone image
img = image[1060:2400,1800:3200].copy()

# Convert color
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.show()

# Save image
filename = 'output-ex2.2.jpg'
cv2.imwrite(filename, image_rgb)