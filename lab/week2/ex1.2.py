import cv2

# Read image
image_path = 'Ex1.jpg'
image = cv2.imread(image_path)

# Show image
image_jpg = cv2.imread('Ex1.jpg', cv2.IMREAD_UNCHANGED)
image_png = cv2.imread('Ex1.png', cv2.IMREAD_UNCHANGED)

print('JPG', image_jpg.shape)
print('PNG', image_png.shape)

# End the GUI
cv2.waitKey(0)
cv2.destroyAllWindows()