import cv2

# Read image
image_path = 'Ex1.jpg'
image = cv2.imread(image_path)

# Show image
# B
cv2.imshow('My Photo', image[:,:,0])
# G
cv2.imshow('My Photo', image[:,:,1])
# R
cv2.imshow('My Photo', image[:,:,2])

# End the GUI
cv2.waitKey(0)
cv2.destroyAllWindows()