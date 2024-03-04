import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex2.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

# Create regtangle
cv2.rectangle(img, (1860,1300), (2900,2700), (8,100,22), 19)

# Create fill regtangle
cv2.rectangle(img, (1860,960), (2500,1300), (22,100,8), cv2.FILLED)

# Make text
cv2.putText(img, 'cat', (2060,1160),cv2.FONT_HERSHEY_TRIPLEX, 3, (0,0,0),20)

# Convert color
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.show()