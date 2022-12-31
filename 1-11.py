import numpy as np, cv2

def fun6_convolutions():
#(1) load image - 0
    #(1) load image - gray
    img = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
    if img is None: print('영상 파일 읽기 오류')
    cv2.imshow("Image_input", img); cv2.waitKey(0) # input image
#(2) define mask weights
    #(2) filter/mask weights:
    weights0 = [1, 1, 1, 1, 1, 1, 1, 1, 1] # Box filter -> / 9
    weights1 = [1, 2, 1, 2, 4, 2, 1, 2, 1] # Gaussian/smoothing / 16
    weights21 = [0, -1, 0, -1, 5, -1, 0, -1, 0] # sharpening - weak
    weights22 = [-1,-1,-1, -1, 9, -1, -1,-1,-1] # sharpening – strong
    # two more … later
#(3) apply_filter x 6 - 1:6
    # 4 steps: (3) Blurring, …
    img_blur = apply_filter (img, weights0, "Blurred_1") ; cv2.waitKey(0)
    #for i in range(1,5):
    img_blur = apply_filter (img_blur, weights0, "Blurred_2") ; cv2.waitKey(0)
    # (3) …, Gaussian smoothing, …
    img_smut = apply_filter (img, weights1, "Smoothed_1") ; cv2.waitKey(0)
    #for i in range(1,5):
    img_smut = apply_filter (img_smut, weights1, "Smoothed_2") ; cv2.waitKey(0)

    # (3) …, …, Sharpening
    img_shar1 = apply_filter (img, weights21, "Sharpen_1") ; cv2.waitKey(0)
    img_shar2 = apply_filter (img, weights22, "Sharpen_2") ; cv2.waitKey(0)
    
#(4) differential filter: Sobel - 7:10
    # (4) Edge detection
    d, d1, d2 = differential (img, weights1, weights22)
    cv2.imshow("Sobel-Gx", d1); cv2.waitKey(0) # Gx image, V-edge
    cv2.imshow("Sobel-Gy", d2); cv2.waitKey(0) # Gy image, H-edge
    cv2.imshow("Sobel-magnit", d); cv2.waitKey(0) # G, edge 크기 영상

    _, d_thr = cv2.threshold(d, 128, 255, cv2.THRESH_BINARY) # 이진
    cv2.imshow("Edge Sobel", d_thr) # binary edge image. 끝.
    
def apply_filter(img, weights, title):
    # create the mask:
    mask = np.array(weights, np.float32).reshape(3,3)
    mask = mask / mask.sum()

    # do the convolution:
    result = filter(img, mask) # float32 matrix
    result = cv2.convertScaleAbs(result) # = 1*result + 0
    cv2.imshow (title, result)
    return result

def filter(img, mask):
    # size, out-image:
    R, C = img.shape[:2]
    dst = np.zeros((R, C), np.float32)
    # mask size, its center coord:
    r, c = mask.shape[:2]
    cy, cx = r//2, c//2
    # do the convolution:
    for i in range(cy, R-cy):
        for j in range(cx, C-cx):
            y1, y2 = i - cy, i+cy+1 # i-image ROI
            x1, x2 = j - cx, j+cx+1
            roi = img[y1:y2, x1:x2].astype('float32')
            prods = cv2.multiply(roi, mask)
            dst[i,j] = cv2.sumElems(prods)[0]
    return dst

def differential(img, W1, W2):
    # create 2 masks:
    mask1 = np.array(W1, np.float32).reshape(3,3)
    mask2 = np.array(W2, np.float32).reshape(3,3)
    # do the convolution:
    d1 = filter(img, mask1) # float32 matrix
    d2 = filter(img, mask2)
    d = cv2.magnitude(d1, d2) # matrix of norms
    d = cv2.convertScaleAbs(d) # G image
    d1 = cv2.convertScaleAbs(d1) # G1 = Gx image
    d2 = cv2.convertScaleAbs(d2) # G2 = Gy image
    return d, d1, d2

fun = 6
if fun == 6:
    fun6_convolutions()

cv2.waitKey(0)
cv2.destroyAllWindows()