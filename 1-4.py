import numpy as np, cv2

def fun8_denoising():
    #(1) input
    img = imread_Lena_gray()
    cv2.imshow("Image_input", img);
    #(2) create a salt-pepper noise image -> (2.2) denoise it
    N = 50000 #2000에서 바꿈
    img1 = add_salt_pepper_noise(img, N)
    ksize = (5, 5)
    img1_b = cv2.blur(img1, ksize) # mean filtering
    img1_G = cv2.GaussianBlur(img1, ksize, N) # Gaussian smoothing
    img1_m = cv2.medianBlur(img1, 5) # median filtering
    titles_1 = ['img1', 'img1_b', 'img1_G', 'img1_m']
    for t in titles_1: cv2.imshow( t, eval(t) )
    #(3) create a Gaussian noise image -> (3.2) denoise iter
    img2 = add_Gaussian_noise(img, 1, N)
    img2_b = cv2.blur(img2, ksize) # mean filtering
    img2_G = cv2.GaussianBlur(img2, ksize, N) # Gaussian smoothing
    img2_m = cv2.medianBlur(img2, 5) # median filtering
    titles_2 = ['img2', 'img2_b', 'img2_G', 'img2_m']
    for t in titles_2: cv2.imshow( t, eval(t) )
    
def imread_Lena_gray():
    img = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('영상 파일 읽기 오류')
        img = np.random.random((512, 512)) * 205
        img = np.uint8(img)
    return img

def add_salt_pepper_noise(img, N):
    R, C = img.shape[:2]
    x, y = np.random.randint(0, C, N), np.random.randint(0, R, N)
    noisy = img.copy()
    for (x, y) in zip(x, y):
        noisy[y, x] = 0 if np.random.rand() < 0.5 else 255
    return noisy

def add_Gaussian_noise(img, sigma, N):
    R, C = img.shape[:2]
    x, y = np.random.randint(0, C, N), np.random.randint(0, R, N)
    noisy = img.copy()
    for (x, y) in zip(x, y):
        noisy[y, x] = np.uint8(np.random.rand() * 255) # ??
    return noisy

fun = 8
if fun == 8:
    fun8_denoising()
    
#키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()