#Sharpening
import cv2
import numpy as np

image = cv2.imread('ahmetcan.jpg', flags=cv2.IMREAD_COLOR)

cv2.imshow('Sharp', image)
cv2.waitKey()
cv2.destroyAllWindows()

kernel = np.array([[0, -1, 0],
                   [-1, 6,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
cv2.imshow('Sharpened', image_sharp)
cv2.waitKey()
cv2.destroyAllWindows()