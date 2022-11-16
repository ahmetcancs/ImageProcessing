#Gama Transformation
import cv2
import numpy as np

img = cv2.imread('picture1.jpg')

for gamma in [3.0, 4.0, 5.0]:
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

    cv2.imwrite('gamma_transformed' + str(gamma) + '.jpg', gamma_corrected)