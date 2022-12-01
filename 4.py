import numpy as np
import cv2

def onChange (value) :
    global image
    dval = value - int(image[0][0]) # 차이값
    image = image + dval
    cv2.imshow(title, image)
    
image = np.zeros((300, 500), np.uint8)
title = 'TB' 
cv2.imshow(title, image)
cv2.createTrackbar('TB', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()