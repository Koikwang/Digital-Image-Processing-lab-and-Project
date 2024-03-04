# Name: Pitchaya, Teerawongpairoj, Sasima Srijanya
# Student-ID: 6388133, 6388196

import cv2
import numpy as np

# Initialize canvas parameters
canvas_size = (600, 600)
canvas = np.ones((canvas_size[1], canvas_size[0], 3), dtype=np.uint8) * 255  # White canvas

drawing = False  # Indicates if drawing mode is active
mode = ''  # Initial drawing mode
last_point = None  # Store the last point for continuous drawing
color = (0, 0, 0) #color template

# function for slider bars
def on_brush_size_change(*args):
    global brush_size
    #global brush_size
    brush_size = cv2.getTrackbarPos("Brush Size", "Drawing Canvas")

def on_color_change(*args):
    global color
    #global color
    color = (cv2.getTrackbarPos("Blue", "Drawing Canvas"),
             cv2.getTrackbarPos("Green", "Drawing Canvas"),
             cv2.getTrackbarPos("Red", "Drawing Canvas"))

# Drawing parameters
def draw_shape(event, x, y, flags, param):
    global canvas, drawing, last_point, color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_point = (x, y)
        if mode == 'circle':
            cv2.circle(canvas, (x, y), 10, color, -1)
        elif mode == 'rectangle':
            param['start_point'] = (x, y)
        elif mode == 'stamp':
            cv2.putText(canvas, '6388133, 6388196', (x, y),cv2.FONT_HERSHEY_TRIPLEX, 1, color, 3)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if mode == 'line':
            if last_point:
                cv2.line(canvas, last_point, (x, y), color, 5)
            last_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_point = None
        if mode == 'rectangle':
           cv2.rectangle(canvas, param['start_point'], (x, y), color, cv2.FILLED)

# Create a GUI window
cv2.namedWindow("Drawing Canvas")
cv2.setMouseCallback("Drawing Canvas", draw_shape, {'start_point': (0, 0)})

# Create slider bars
cv2.createTrackbar("Red", "Drawing Canvas", color[2], 255, on_color_change)
cv2.createTrackbar("Blue", "Drawing Canvas", color[0], 255, on_color_change)
cv2.createTrackbar("Green", "Drawing Canvas", color[1], 255, on_color_change)

while True:
    cv2.imshow("Drawing Canvas", canvas)

    key = cv2.waitKey(1)
    
    if key == ord('c'):   # switch to circle drawing mode
        mode = 'circle'
    elif key == ord('r'): # switch to rectangle drawing mode
        mode = 'rectangle'
    elif key == ord('s'): # switch to stamp drawing mode
        mode = 'stamp'
    elif key == ord('l'): # switch to line drawing mode
        mode = 'line'
    elif key == ord('q'): # exit
        # End the GUI
        cv2.destroyAllWindows()
        break