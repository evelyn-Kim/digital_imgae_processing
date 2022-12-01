import numpy as np, cv2

def fun10_locate_faces():
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
    mc_im = cv2.morphologyEx(face, cv2.MORPH_CLOSE, mask3, iterations=2)
    mco = cv2.morphologyEx(mc_im, cv2.MORPH_OPEN, mask3, iterations=2)
    cv2.imshow('M_CloseOpen', mco); cv2.waitKey(0) # (w6) = d2e4d2
    #(4) morphological processing 2
    mfaces = mco
    fcontours = locateFaces(mfaces)
    cv2.imshow('Face_contours', fcontours); cv2.waitKey(0) # (w7)
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
                   
def locateFaces(mfaces): # mfaces = white contours on black background
    canny = cv2.Canny(mfaces[:,:,0], 100, 200, 3) # 3 = apperture (3x3)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #(4) read each contour, and draw it all onto an output image
    # drawing = mfaces
    drawing = np.zeros(mfaces.shape, np.uint8) # RGB
    for c in contours:
        color = (int(np.random.uniform(0,255)), int(np.random.uniform(0,255)), int(np.random.uniform(0,255)))
        cv2.drawContours(drawing, [c], -1, color, 2, 8)
        #-- fitting contour c with a rectangle & ellipse:
        if cv2.contourArea(c) > 1000: #or True:
            drawing = drawREBound1(drawing, c, color)
    return drawing

def drawREBound1(fcon_img, contr, color):
    #- fit a Rectangle to the contour
    rrect1 = cv2.minAreaRect(contr) # fit/find
    box = cv2.boxPoints(rrect1)
    points4 = np.int0(box)
    fcon_img = cv2.polylines(fcon_img, [points4], True, color, 1) #draw it
    #- fit & draw an ellipse to the contour
    rrect2 = cv2.fitEllipse (contr) # fit/find
    fcon_img = cv2.ellipse(fcon_img, rrect2, color, 1, 8) #draw it
    return fcon_img
    
fun = 10
if fun == 10:
    fun10_locate_faces()
    
#키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()