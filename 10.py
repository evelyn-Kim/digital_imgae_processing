from cv2 import resize
import numpy as np
import cv2

def onThreshold_H0(value):
    th[0] = cv2.getTrackbarPos("H_thresh1", "result")
    th[1] = cv2.getTrackbarPos("H_thresh2", "result")
    # thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    _, res_im2 = cv2.threshold(res_im, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im2, th[0], 255, cv2.THRESH_BINARY, res_im2)
    cv2.imshow ("result", res_im2)

    mask = cv2.inRange(Hsv, (th[0], 0, 0), (th[1], 255, 255))
    mask_i = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(resize, resize, mask = mask_i)
    cv2.imshow('mask-man', mask_i)
    cv2.imshow('image-man', result)
    b_p = cv2.bitwise_and(b, mask)
    cv2.imshow('image-bg', b_p)
    
fun = 5
if fun == 5:
    #(1) load image, (2) convert colormap
    Bgr = cv2.imread("weatherman-on-green2.jpg", cv2.IMREAD_COLOR)
    b = cv2.imread("weather-map.jpg", cv2.IMREAD_COLOR)[0:660,0:442]
    resize = cv2.resize(Bgr,(490, 408))
    Hsv = cv2.cvtColor (Bgr, cv2.COLOR_BGR2HSV) # 변환
    hue =np.copy (Hsv[:,:,0])
    bb = cv2.imread("weatherman-on-green2.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("BGR input", Bgr)
    cv2.namedWindow("result")
    #(3) create trackbars with CB function(s)
    th = [50, 100]
    cv2.createTrackbar ("H_thresh1", "result", th[0], 255, onThreshold_H0)
    cv2.createTrackbar ("H_thresh2", "result", th[1], 255, onThreshold_H0)
    


cv2.waitKey(0)
cv2.destroyAllWindows()