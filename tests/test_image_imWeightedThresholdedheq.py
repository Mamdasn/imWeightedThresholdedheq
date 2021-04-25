import numpy as np 
from imWeightedThresholdedheq import imWTHeq
import cv2


image = cv2.imread('assets/Plane.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_v = image_hsv[:, :, 2].copy()

image_v_heq, _= imWTHeq(image_v, r=0.5, v=0.5)

image_hsv[:, :, 2] = image_v_heq.copy()
image_heq = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite('assets/Plane-imWeightedThresholdedheq.jpg', image_heq)

