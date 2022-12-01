import numpy as np
import cv2

img = np.full ((300,500,3),(255,255,255), np.uint8)
p1 = (-1,-1)
title = "Canvas"
red, blue = (0,0,255), (255,0,0)
c = red

def onMouse (event, x, y, flags, par):
    global p1, red, blue, c
    if event == cv2.EVENT_LBUTTONDOWN: #왼쪽 버튼을 누르면 
        c = red
    elif event == cv2.EVENT_RBUTTONDOWN: #오른쪽 버튼을 누르면
        c = blue
    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:#손을 뗄 때는 
        p1 = (-1,-1) #그림을 그리지 않음
        return
    elif event == cv2.EVENT_MOUSEMOVE: #마우스를 움직이면
        if p1[0] == -1: #그려지지 않을 때, 아무것도 안하는 상태
            return
    else: 
        return

    p = (x, y)
    if p1[0] >= 0:
        cv2.line(img, p1, p, c, 3, cv2.LINE_8)
        cv2.imshow(title, img)
    p1 = p
    
cv2.imshow("Canvas" , img)
cv2.setMouseCallback ("Canvas" , onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()