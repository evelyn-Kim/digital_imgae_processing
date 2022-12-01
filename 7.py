import numpy as np, cv2

def fun_masking():
    img0 = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
    if img0 is None:
        print('error')
        img0 = np.random.random((512,512)) * 255 # 랜덤 영상 만들기
        img0 = np.uint8(img0)
    print('img0 :', img0.shape)
    mask3 = np.zeros(img0.shape, np.uint8) # a mask to be
    mask6 = np.zeros(img0.shape, np.uint8) # another mask to be
    pts3 = np.array([[256, 100], [406, 400], [106, 400]], np.int32) # 삼각형3꼭지
    pts6 = np.array([[256, 100], [286, 286], [406, 400], [256, 330], [106, 400], [226, 286]], np.int32)
    mask3 = cv2.fillPoly(mask3, [pts3], 255) # triangle-fill
    mask6 = cv2.fillPoly(mask6, [pts6], 255) # Benz
    cv2.namedWindow('image-in', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image-in', img0)
    cv2.imshow('mask3', mask3)
    cv2.imshow('mask6', mask6)
    cv2.imshow('image-out', cv2.bitwise_and(img0, mask3))
    cv2.imshow('image-out6', cv2.bitwise_and(img0, mask6))
    
fun = 1
if fun == 1: fun_masking()
cv2.waitKey(0)
cv2.destroyAllWindows()