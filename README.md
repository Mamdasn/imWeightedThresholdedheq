# imWeightedThresholdedheq
This module attempts to enhance contrast of a given image by employing a method called weighted thresholded histogram equalization (WTHE). This method seeks to improve on preformance of the conventional histogram equalization method by adding controllable parameters to it. By weighting and thresholding the PMF of the image before performing histogram equalization, two parameters are introduced that can be changed manually, but by experimenting on a variety of images, optimal values for both parameters are calculated (r = 0.5, v = 0.5).

You can access the article that came up with this method [here](https://www.researchgate.net/publication/3183125_Ward_RK_Fast_ImageVideo_Contrast_Enhancement_Based_on_Weighted_Thresholded_Histogram_Equalization_IEEE_Trans_Consumer_Electronics_532_757-764).  


## Installation

Run the following to install:

```python
pip install imWeightedThresholdedheq
```

## Usage

```python
import numpy as np
import cv2
from imWeightedThresholdedheq import imWTHeq 

cap = cv2.VideoCapture('assets/Arctic-Convoy-With-Giant-Mack-Trucks.mp4')

# output video without sound
video_out_name = 'assets/output.mp4'
i = 0
j = 0
Wout_list = np.zeros((10))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_v   = frame_hsv[:, :, 2].copy()
    image_heq, Wout = imWTHeq(frame_v, Wout_list, r=0.5, v=0.5)
    Wout_list[j] = Wout
    j += 1
    if j == 10:
        j = 0
    frame_hsv[:, :, 2] = image_heq
    frame_eq = cv2.cvtColor(frame_hsv, cv2.COLOR_HSV2BGR)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if i==0:
        h, w, d = frame_eq.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_out = cv2.VideoWriter(video_out_name, fourcc, fps, (w, h))
    video_out.write(frame_eq)

    i+=1
cv2.destroyAllWindows()
video_out.release()
```

## Showcase
* A 5 minutes comparative video: https://youtu.be/5H_EY_ugmzg
* This is a sample video  
[![Arctic-Convoy-With-Giant-Mack-Trucks.gif GIF](https://raw.githubusercontent.com/Mamdasn/imWeightedThresholdedheq/main/assets/Arctic-Convoy-With-Giant-Mack-Trucks.gif "Arctic-Convoy-With-Giant-Mack-Trucks.gif GIF")](https://youtu.be/5H_EY_ugmzg)  
The sample video enhanced by WTHE method  
[![Arctic-Convoy-With-Giant-Mack-Trucks-imWeightedThresholdedheq.gif GIF](https://raw.githubusercontent.com/Mamdasn/imWeightedThresholdedheq/main/assets/Arctic-Convoy-With-Giant-Mack-Trucks-imWeightedThresholdedheq.gif "Arctic-Convoy-With-Giant-Mack-Trucks-imWeightedThresholdedheq.gif GIF")](https://youtu.be/5H_EY_ugmzg)  
