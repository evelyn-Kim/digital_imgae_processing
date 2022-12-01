from cv2 import resize
import numpy as np
import cv2

#onTreshold 정의
def onThreshold_H(value):
    th[0] = cv2.getTrackbarPos("H_thresh1", "result") #트랙바 "H_thresh1"의 현재 위치를 반환해준다.(윈도우 이름이 "result")
    th[1] = cv2.getTrackbarPos("H_thresh2", "result") #트랙바 "H_thresh2"의 현재 위치를 반환해준다.(윈도우 이름이 "result")
    _, res_im = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV) #hue에 임계처리를 해준다. THRESH_TOZERO_INV 종류 사용
    _, res_im2 = cv2.threshold(res_im, th[1], 255, cv2.THRESH_TOZERO_INV) #res_im에 임계처리를 해준다. THRESH_TOZERO_INV 종류 사용
    cv2.threshold(res_im2, th[0], 255, cv2.THRESH_BINARY, res_im2) #res_im2에 임계처리를 해준다. THRESH_BINARY 종류 사용
    cv2.imshow ("result", res_im2) #윈도우 이름이 "result"인 창에 res_im2를 보여준다.

    mask = cv2.inRange(Hsv, (th[0], 0, 0), (th[1], 255, 255)) #이미지 영역을 추출한다.
    mask_n = cv2.bitwise_not(mask) #bitwise_not을 실행한다. 이미지의 반전을 실행한다
    mask_b = cv2.bitwise_and(b, b, mask = mask) #mask와 b의 중첩된 부분을 추출한다.
    result = cv2.bitwise_and(resize, resize, mask = mask_n) #mask_n과 resize의 중첩된 부분을 추출한다.
    b_p = cv2.bitwise_and(b, mask_b) #이미지 b와 mask_b의 중첩된 부분을 추출한다.
    r_b= cv2.add(result, b_p) #이미지 rsult와 b_p를 더한다.
    cv2.imshow('mask-man', mask_n) #이미지 화면 출력
    cv2.imshow('image-man', result) #이미지 화면 출력
    cv2.imshow('image-bg', b_p) #이미지 화면 출력
    cv2.imshow('image-TV', r_b) #이미지 화면 출력
    
fun = 1
if fun == 1:
    Bgr = cv2.imread("weatherman-on-green2.jpg", cv2.IMREAD_COLOR) #저장된 이미지 읽어 오기 (color로 읽기)
    b = cv2.imread("weather-map.jpg", cv2.IMREAD_COLOR)[0:408,0:490] #저장된 이미지 읽어 오기/크기 변환하기
    resize = cv2.resize(Bgr,(490, 408))#크기 변환하기
    Hsv = cv2.cvtColor(Bgr, cv2.COLOR_BGR2HSV) # 색상 공간을 변경
    hue =np.copy(Hsv[:,:,0]) #이미지 복사하기
    bb = cv2.imread("weatherman-on-green2.jpg", cv2.IMREAD_GRAYSCALE) #저장된 이미지 읽어 오기 (grayscale로 읽기)
    cv2.imshow("BGR input", Bgr) #이미지 화면 출력
    cv2.namedWindow("result") #윈도우 이름이 "result"인 창 만들기
    th = [50, 100] #th 리스트
    #트랙바 생성하기(트랙바 이름은 "H_thresh1", 윈도우 이름은 "result", 트랙바 시작값은 th[0] = 50부터 끝은 255까지, onThreshold_H 콜백함수)
    cv2.createTrackbar ("H_thresh1", "result", th[0], 255, onThreshold_H) 
    #트랙바 생성하기(트랙바 이름은 "H_thresh2", 윈도우 이름은 "result", 트랙바 시작값은 th[1] = 100부터 끝은 255까지, onThreshold_H 콜백함수)
    cv2.createTrackbar ("H_thresh2", "result", th[1], 255, onThreshold_H)
    
#키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()