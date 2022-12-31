import numpy as np, cv2
def fun12_HoughLines():
    #(0) global vars
    global img, gim, wimg, wmap
    #(1) read image
    img = cv2.imread("OntarioHighway.png", cv2.IMREAD_COLOR)
    wimg, wmap = "OntarioHighway", "Edge"
    cv2.namedWindow(wimg, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(wimg, img)
    #(2) convert to gray, and smooth it (for Canny + Hough)
    gim = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gim = cv2.GaussianBlur(gim, (3, 3), 0, 0)
    cv2.imshow(wmap, gim)
    #(3) create 3 track bars
    cv2.createTrackbar ("Tbar_1", wmap, thC[0], 255, onThreshold_Canny);
    cv2.createTrackbar ("Tbar_2", wmap, thC[1], 255, onThreshold_Canny2);
    cv2.createTrackbar ("Tbar_3", wmap, thH, 200, onThreshold_Hough);
# 2 top level variables
thC = [130, 255] # Canny’s thresholds
thH = 130 # Hough's threshold (# pixels)
def onThreshold_Canny(value):
    global thC
    thC[0] = cv2.getTrackbarPos("Tbar_1", wmap) #최소
    #thC[1] = cv2.getTrackbarPos(“Tbar_2“, wmap)
    canny = hough_liner() # gim -> canny -> draw lines
    cv2.imshow(wmap, canny)

    res = houghpr_liner() # gim -> canny -> draw lines on img.copy
    cv2.imshow(wimg, res)
def onThreshold_Canny2(value):
    global thC
    #thC[0] = cv2.getTrackbarPos(“Tbar_1“, wmap)
    thC[1] = cv2.getTrackbarPos("Tbar_2", wmap)  #최대
    canny = hough_liner() # gim -> canny -> draw lines
    cv2.imshow(wmap, canny)
    #원래 영상에 빨간 선분을 그려놓음
    res = houghpr_liner() # gim -> canny -> draw lines on img.copy
    cv2.imshow(wimg, res)
def onThreshold_Hough(value):
    global thH
    thH = cv2.getTrackbarPos("Tbar_3", wmap)
    canny = hough_liner() # gim -> canny -> draw lines
    cv2.imshow(wmap, canny)
    #원래 영상에 빨간 선분을 그려놓음
    res = houghpr_liner() # gim -> canny -> draw lines on img.copy
    cv2.imshow(wimg, res)
def hough_liner(): 
    canny = cv2.Canny(gim, thC[0], thC[1]) # 실행 -> Canny 경계 검출
    #원래 영상에 빨간 선분을 그려놓음
    lines = cv2.HoughLines(canny, 0.5, np.pi/180, thH)
    # ,rho,theta,thr(0~1), 각도구간, 픽셀수
    white = 255
    for i in range(len(lines)): # 실행 -> Canny 경계 위에 Hough 직선 검출
        for rho, theta in lines[i]:
            a, b = np.cos(theta), np.sin(theta)
            x0, y0 = a*rho, b*rho
            x1, y1 = int(x0 + 1000*(-b)), int(y0+1000*(a))
            x2, y2 = int(x0 - 1000*(-b)), int(y0 -1000*(a))
            cv2.line(canny, (x1, y1), (x2, y2), white, 2)
    return canny
def houghpr_liner(): # 실행 -> Canny 경계 위에 Hough 직선 검출 -> 원 영상에 출력
    canny = cv2.Canny(gim, thC[0], thC[1])
    res = img.copy() # input, color image
    minLineLength, maxLineGap = 100, 20 # 선분 최소길이, 선분간 최대 허용간극
    red = (0, 0, 255)
    lines = cv2.HoughLinesP(canny, 0.5, np.pi/180, thH, minLineLength, maxLineGap)
    # ,rho,theta,thr(0~1), 각도구간, 픽셀수, 선분 최소길이, 선분간 최대 허용간극
    for i in range(len(lines)):
        for x1,y1, x2,y2 in lines[i]:
            cv2.line(res, (x1, y1), (x2, y2), red, 3)
    return res


fun = 12
if fun == 12:
    fun12_HoughLines()
    
cv2.waitKey(0)
cv2.destroyAllWindows()