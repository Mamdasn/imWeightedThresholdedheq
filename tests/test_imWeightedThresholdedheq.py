import numpy as np
import cv2
from imWeightedThresholdedheq import imWTHeq

def test_im2dhisteq_with_param():
    
    image_name = '../assets/Plane.jpg'
    image = cv2.imread(image_name)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_v = image_hsv[:, :, 2].copy()
    image_v_heq, _= imWTHeq(image_v, r=0.5, v=0.5)
    
    # np.save(f'{image_name}-WTHE', image_v_heq)

    image_v_heq_cmpr = np.load(f'{image_name}-WTHE.npy')
    assert np.all(image_v_heq == image_v_heq_cmpr)

    
    
