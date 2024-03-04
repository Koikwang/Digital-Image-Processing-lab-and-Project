# Name: Pitchaya, Teerawongpairoj, Sasima Srijanya
# Student-ID: 6388133, 6388196

import cv2
import numpy as np

# Callback function for the slider bars
def on_slider_change(*args):
    global scale_percent
    global copy_image
    scale_percent = cv2.getTrackbarPos("Scale", window_name) / 100
    new_width = int(image.shape[1] * scale_percent)
    new_height = int(image.shape[0] * scale_percent)
    copy_image = cv2.resize(image, (new_width, new_height))
    brightness = cv2.getTrackbarPos("Brightness", window_name)
    adjusted_image = cv2.convertScaleAbs(copy_image, alpha=1.0, beta=brightness)

    # Create the black background
    black_background = np.zeros((height, width, 3), dtype=np.uint8)

    # Overlay the adjusted image onto the black background
    y_offset = (height - adjusted_image.shape[0]) // 2
    x_offset = (width - adjusted_image.shape[1]) // 2
    black_background[y_offset:y_offset + adjusted_image.shape[0], x_offset:x_offset + adjusted_image.shape[1]] = adjusted_image

    # Create a copy of the black background to add text
    gui_image = black_background.copy()

    # Add text to the adjusted image
    text = "Scale: {:.2f}, Brightness: {}".format(scale_percent, brightness)
    cv2.putText(gui_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    text1 = "6388133 Pitchaya Teerawongpairoj"
    cv2.putText(gui_image, text1, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    text2 = "6388196 Sasima Srijanya"
    cv2.putText(gui_image, text2, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    cv2.imshow(window_name, gui_image)

# Load an image
image = cv2.imread("kj.jpg")

# Set initial values
scale_percent = 0.05
height, width = 680, 940

# Create a named window
window_name = "Resizing GUI"
cv2.namedWindow(window_name)

# Create slider bars
cv2.createTrackbar("Scale", window_name, int(scale_percent * 100), 100, on_slider_change)
cv2.createTrackbar("Brightness", window_name, 0, 255, on_slider_change)

# Initialize copy_image
copy_image = cv2.resize(image, (int(image.shape[1] * scale_percent), int(image.shape[0] * scale_percent)))

# Show the initial GUI
on_slider_change()

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):  # q to exit
        break

# End GUI
cv2.destroyAllWindows()
