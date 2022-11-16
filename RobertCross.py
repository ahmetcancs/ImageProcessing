#RobertCross
import cv2
import numpy as np
from scipy import ndimage
roberts_cross_v = np.array([[1, 0],
                            [0, -1]])

roberts_cross_h = np.array([[0, 1],
                            [-1, 0]])

img = cv2.imread("picture1.jpg", 0).astype('float64')
img /= 255.0
vertical = ndimage.convolve(img, roberts_cross_v)
horizontal = ndimage.convolve(img, roberts_cross_h)

roberts_cross = np.sqrt(np.square(horizontal) + np.square(vertical))
roberts_cross *= 255
cv2.imshow("Robert's Cross", roberts_cross)

cv2.waitKey(0)
cv2.destroyAllWindows()