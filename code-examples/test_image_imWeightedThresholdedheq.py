import numpy as np 
from imWeightedThresholdedheq import imWTHeq
import cv2
import os

filename = 'assets/Plane.jpg'
image = cv2.imread(filename)
name, ext = os.path.splitext(filename)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_v = image_hsv[:, :, 2].copy()

image_v_heq, _= imWTHeq(image_v, r=0.5, v=0.5)

image_hsv[:, :, 2] = image_v_heq.copy()
image_heq = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite(f'{name}-imWeightedThresholdedheq{ext}', image_heq)

