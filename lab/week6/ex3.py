import cv2
import numpy as np

# Load the video
video_path = 'Ex2-focus.mp4'
cap = cv2.VideoCapture(video_path)

# Initialize variables to keep track of the frame with maximum blur
max_blur = -1
max_blur_frame = -1
frame_number = 0

while True:
    # Read the next frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the variance of Laplacian to measure blur
    blur = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Update the frame with maximum blur
    if blur > max_blur:
        max_blur = blur
        max_blur_frame = frame.copy()
        frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

# Release the video capture object
cap.release()

# Display the frame with maximum blur and its frame number
cv2.imshow(f"Frame {frame_number}", max_blur_frame)
print(f"Frame {frame_number} has the maximum blur with a variance of Laplacian: {max_blur}")

# Wait for a key press and then close the OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
