import cv2
import numpy as np

def fun4_hist_processing(img):
    histSize, ranges = [32], [0, 256] # num-of-bins (32), bin boundaries?
    hist2 = cv2.calcHist([img], [0], None, histSize, ranges)
    v2 = np.max(hist2)
    gap = 256/histSize[0] # 256/32 = 8 = bin_w
    histWShape = (200, 256) # histogram window shape
    #- (2) drawing hist : hist -> hist_img : histShape -
    hist_img = np.zeros(histWShape, np.uint8) + 255
    cv2.normalize(hist2, hist2, 0, histWShape[0], cv2.NORM_MINMAX)
    cv2.rectangle(hist_img, (0, 0, histWShape[1], histWShape[0]), 200)
    for i, h in enumerate(hist2):
        x = int(i*gap)
        w = int(gap)
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    cv2.flip(hist_img, 0, hist_img)
    cv2.putText(hist_img, '0', (0, histWShape[0]), \
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,0,255))
    cv2.putText(hist_img, str(int(v2)), (0, histWShape[0]*0+12), \
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,0,255))
    # - imshow img, hist_img - 
    cv2.imshow('image-red', img)
    cv2.imshow('histogram2', hist_img)
    cv2.waitKey(0) # 바로 앞에 추가 한다 – 단계별 수행…
    #(3) <- histogram stretching -
    #- 3.1 LUT 만들기 – 
    IDX = create_IDX_table(hist2, histSize)
    # # - 3.2 LUT 적용하여 영상 변환! 결과 출력
    img_stretched = cv2.LUT(img, IDX.astype('uint8'))
    cv2.imshow('img-H-stretched', img_stretched)
    # - 3.3 결과 영상 histogram 그려 확인
    hist_s = cv2.calcHist([img_stretched], [0], None, histSize, ranges)
    hist_img_s = draw_histogram(hist_s, histWShape) # -> 함수!
    cv2.imshow('histogram-stretched', hist_img_s)
    cv2.waitKey(0) # 바로 앞에 추가 한다 – 단계별 수행…
    #(4)
    img_eqd = cv2.equalizeHist(img) # 평활화 결과 영상 바로 출력
    cv2.imshow('image-H-eqd', img_eqd)
    hist_eq = cv2.calcHist([img_eqd], [0], None, histSize, ranges)
    hist_img_eq = draw_histogram(hist_eq, histWShape)
    cv2.imshow('histogram-eqd', hist_img_eq)
    #(4) H-평활화 실습 –끝

def create_IDX_table(hist, histSize):
    bin_w = 256 / histSize[0]
    low = search_index2_boundary(hist, 0) * bin_w   
    high = search_index2_boundary(hist, histSize[0]-1) * bin_w
    
    IDX = np.arange(0, 256) #table 
    IDX = (IDX - low) / (high - low) * 255 #ex. [..-4 -2 0 2 4 ... 258 ..]
    IDX[0:int(low)] = 0
    IDX[int(high+1):] = 255
    return IDX.astype('uint8')

def search_index2_boundary(hist, bias=0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        if hist[idx] > 0: return idx
    return -1

def draw_histogram(hist, shape=(200,256)):
    v2 = np.max(hist)
    bin_w = shape[1] / hist.shape[0]
    
    hist_img = np.zeros(shape, np.uint8) + 255
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    cv2.rectangle(hist_img, (0, 0, shape[1], shape[0]), 200)
    for i, h in enumerate(hist):
        x = int(i*bin_w)
        w = int(bin_w)
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    cv2.flip(hist_img, 0, hist_img)
    cv2.putText(hist_img, '0', (0, shape[0]), \
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,0,255))
    cv2.putText(hist_img, str(int(v2)), (0, shape[0]*0+12), \
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,0,255))
    return hist_img


img0 = cv2.imread('Lena.png', cv2.IMREAD_COLOR)
if img0 is None:
    print('영상 파일 읽기 오류')
img = np.copy(img0)
fun = 4
if fun == 4:
    fun4_hist_processing(img[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()