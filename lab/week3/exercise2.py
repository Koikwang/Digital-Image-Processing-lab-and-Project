import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'Ex2-gray.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

# Appling colormap
img_hot = cv2.applyColorMap(img, cv2.COLORMAP_DEEPGREEN)

# Convert color
image_rgb = cv2.cvtColor(img_hot, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.show()

# End the GUI
cv2.waitKey(0)
cv2.destroyAllWindows()