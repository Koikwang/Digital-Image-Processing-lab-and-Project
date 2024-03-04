import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Ex2-periodicNoise.jpg', cv2.IMREAD_GRAYSCALE)  # Load the image in grayscale

# Apply FFT
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Calculate magnitude spectrum and normalize
magnitude_spectrum = np.log(np.abs(f_transform_shifted))

# Inverse FFT to denoise
f_transform_inverse = np.fft.ifftshift(f_transform_shifted)
image_denoised = np.fft.ifft2(f_transform_inverse)
image_denoised = np.abs(image_denoised)

# Normalize the denoised image to [0, 255]
image_denoised = cv2.normalize(image_denoised, None, 0, 255, cv2.NORM_MINMAX)

# Convert to uint8 for displaying
image_denoised = np.uint8(image_denoised)

# Display the images
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Spectrum')
plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(image_denoised, cmap='gray')
plt.title('Denoised Image')
plt.xticks([]), plt.yticks([])

plt.show()
