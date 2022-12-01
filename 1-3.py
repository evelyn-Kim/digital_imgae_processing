import numpy as np, cv2

th = [100, 150]
def fun7_Canny():
    global img
    img = imread_Lena_gray()
    cv2.imshow('Image_input', img)
    #(2) windows &trackbars - Canny's output
    cv2.namedWindow('WinCanny', cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar('Tbar_1', 'WinCanny', th[0], 255, onThreshold_Canny)
    cv2.createTrackbar('Tbar_2', 'WinCanny', th[1], 255, onThreshold_Canny2)

def imread_Lena_gray():
    img = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('error')
        img = np.random.random((512,512))*205
        img = np.uint8(img)
    return img 

def onThreshold_Canny(value):
    # read trackbar positions:
    th[0] = cv2.getTrackbarPos('Tbar_1', 'WinCanny')
    #th[1] = cv2.getTrackbarPos('Tbar_2', 'WinCanny')
    # compute the Canny edge:
    canny = cv2.Canny(img, th[0], th[1])
    cv2.imshow ('WinCanny', canny)

def onThreshold_Canny2(value):
    # read trackbar positions:
    #th[0] = cv2.getTrackbarPos('Tbar_1', 'WinCanny')
    th[1] = cv2.getTrackbarPos('Tbar_2', 'WinCanny')
    # compute the Canny edge:
    canny = cv2.Canny(img, th[0], th[1])
    cv2.imshow ('WinCanny', canny)
 
fun = 7
if fun == 7:
    fun7_Canny()
    
#키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()