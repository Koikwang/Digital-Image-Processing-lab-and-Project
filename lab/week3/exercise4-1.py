import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_grammar(img, grammar):
    img = img.astype(np.double)
    adjusted_grammar = np.clip(np.power(img, grammar), 0, 255).astype(np.uint8)
    return adjusted_grammar

# Read image
image_path = 'Ex2-gray.jpg'
image = cv2.imread(image_path)

# Clone image
img = image.copy()

grammar = 1.5

# Adjust grammar
adjusted_grammar_image = adjust_grammar(img, grammar)
plt.imshow(adjusted_grammar_image, cmap='gray')
plt.title('Adjusted grammar')
plt.show()