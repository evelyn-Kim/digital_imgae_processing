from cv2 import resize
import numpy as np
import cv2

def onThreshold_H0(value):
    th[0] = cv2.getTrackbarPos("H_thresh1", "result")
    # thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im, th[0], 255, cv2.THRESH_BINARY, res_im)
    cv2.imshow ("result", res_im)
    # chroma_key -> Homework #2
    
def onThreshold_H1(value):
    th[1] = cv2.getTrackbarPos("H_thresh2", "result")
    # thresholding:
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(res_im, th[0], 255, cv2.THRESH_BINARY, res_im)
    cv2.imshow ("result", res_im)
    
fun = 5
if fun == 5:
    #(1) load image, (2) convert colormap
    Bgr = cv2.imread("weatherman-on-green2.jpg", cv2.IMREAD_COLOR)
    resize = cv2.resize(Bgr,(490, 408))
    Hsv = cv2.cvtColor (Bgr, cv2.COLOR_BGR2HSV) # 변환
    hue =np.copy (Hsv[:,:,0])
    cv2.imshow("BGR input", Bgr)
    cv2.namedWindow("result")
    #(3) create trackbars with CB function(s)
    th = [50, 100]
    cv2.createTrackbar ("H_thresh1", "result", th[0], 255, onThreshold_H0)
    cv2.createTrackbar ("H_thresh2", "result", th[1], 255, onThreshold_H1)
    h = cv2.getTrackbarPos('H_thresh1', 'result')
    h2 = cv2.getTrackbarPos('H_thresh2', 'result')
    print(h, h2)
    lower = np.array(h)
    upper = np.array(h2)
    mask = cv2.inRange(resize, lower, upper)
    result = cv2.bitwise_and(resize, resize, mask=mask)
    cv2.imshow('output', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()