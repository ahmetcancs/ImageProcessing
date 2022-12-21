from PIL import Image
import numpy as np
import cv2

# Open the image and convert it to grayscale
image = Image.open('picture1.jpg').convert('L')

# Convert the image to a numpy array
image_array = np.array(image)

# Perform an opening operation to remove small objects
kernel = np.ones((3,3), np.uint8)
opened_array = cv2.morphologyEx(image_array, cv2.MORPH_OPEN, kernel)

# Find the edges of the image using the Canny edge detection algorithm
edges = cv2.Canny(opened_array, 100, 200)

# Convert the edges array back to an image and save it
edges_image = Image.fromarray(edges)
edges_image.save('edges.jpg')