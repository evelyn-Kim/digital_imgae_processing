import numpy as np, cv2

def fun9_face_morphology():
    #(1) input
    img = cv2.imread('worldleaders_atUN.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('Input', img); # (w0)
    cv2.waitKey(0)
    #(2) skin_color_processor
    face = skin_color_processor(img)
    cv2.imshow('Face', face) # (w1)
    cv2.waitKey(0)
    #(3) morphological processing 1
    mask3 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')
    d_img = cv2.dilate(face, mask3) # (w2)
    cv2.imshow('Dilate', d_img); cv2.waitKey(0)
    e_img = cv2.erode(face, mask3) # (w3)
    cv2.imshow('Erode', e_img); cv2.waitKey(0)
    de_img = cv2.erode(d_img, mask3) # (w4)
    cv2.imshow('D1+E1', de_img); cv2.waitKey(0) # 효과 = ‘close‘ 연산
    #(4) morphological processing 2
    d2_img = cv2.dilate(d_img, mask3) # d2 = dilate^2
    d2e_img = cv2.erode(d2_img, mask3)
    d2e2_img = cv2.erode(d2e_img, mask3)
    cv2.imshow('D2+E2', d2e2_img); cv2.waitKey(0) # (w5), ‘close^2’ # 계속: .erode(d2e2) -> .erode -> .dilate -> .dilate -> d2e4d2_img
    # = + ‘open^2’ 
    #(5) morphological processing 3:  효과: open2 = e2d2, close2 = d2e2
    mo_im = cv2.morphologyEx(face, cv2.MORPH_OPEN, mask3, iterations=2)
    mc_im = cv2.morphologyEx(face, cv2.MORPH_CLOSE, mask3, iterations=2)
    mco = cv2.morphologyEx(mc_im, cv2.MORPH_OPEN, mask3, iterations=2)
    cv2.imshow('M_CloseOpen', mco); cv2.waitKey(0) 


def skin_color_processor(img): # img = BGR
    R, C = img.shape[:2]
    skin = np.zeros((R, C, 3), np.uint8)
    for i in range(0, R):
        for j in range(0, C):
            if isskin(img[i, j]): skin[i, j] = 255
    return skin
                    
def isskin(bgr):
    return isskin_Peer(bgr[2], bgr[1], bgr[0])
    
def isskin_Peer(r, g, b):
    r_b = abs(r.astype('int16') - b.astype('int16'))
    if not(r > 95 and g > 40 and b > 20): 
        return False
    elif not(r_b > 15 and (r > g) and (r > b)): 
        return False
    else:
        mx = max(r, g)
        mn = min(r, b)
        if (max(mx, b) - min(mn, b) <= 15): return False
        else: return True

fun = 9
if fun == 9:
    fun9_face_morphology()
    
#키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()