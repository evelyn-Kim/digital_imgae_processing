from ctypes import sizeof
import numpy as np
import cv2

#p1, red, c, p0, ptv, n 지정
p1 = (-1,-1)
red = (0, 0, 255)
c = red
p0 = p1
ptv = np.array([[0,0]]) #배열
n = 0

#마스크 추출을 위한 마우스 클릭 이벤트 정의
def onMouse(event, x, y, flag, par):
    global p1, red, c, p0, ptv, n #전역변수 지정
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼을 누르면
        c = red #색은 red
    elif event == cv2.EVENT_RBUTTONDOWN:  # 오른쪽 버튼을 누르면
        if n > 0: # n>0 이면
            p = (x,y) #p는 좌표
            cv2.line(img0, p1, p, c, 3, cv2.LINE_8) #선을 그린다
            cv2.line(img0, p0, p, c, 3, cv2.LINE_8) #선을 그린다
            cv2.imshow("image-in", img0) #img0 출력
            ptv = np.append(ptv, [[x,y]], axis = 0); n = n+1 #ptv에 좌표를 추가, n = n+1
            print('ptv=', ptv) #ptv 출력
            p1 = (-1, -1); n = 0 #p1 좌표, n은 0
            mask = np.zeros(img0.shape, np.uint8) #mask는 img0크기만큼 0으로 채우기
            mask = cv2.fillPoly(mask,[ptv], 255) #mask에 [ptv]로 이뤄진 내부가 채워지지않은 다각형 그리기
            cv2.imshow('image-out1', cv2.bitwise_and(img0, mask)) #img0와 mask에 중첩된 부분을 추출 및 보여주기
            cv2.imshow('image-out2', cv2.subtract(img_r, mask)) #img_r과 mask에 중첩된 부분을 빼기 및 보여주기
            cv2.imshow('image-out3', cv2.add(cv2.subtract(img_r, mask), cv2.bitwise_and(img0, mask))) #마스크 이미지끼리 더하기
            print('$ Points too few!') #출력
            return #반환
    else:  #그렇지 않으면
        return #반환
    
    p = (x, y) #좌표
    if p1[0] >= 0: #p1[0] >= 0이면
        cv2.line(img0, p1, p, c, 3, cv2.LINE_8) #선을 그린다
        cv2.imshow('image-in', img0) #img0 출력
        ptv = np.append(ptv, [[x,y]], axis = 0) #ptv에 좌표를 추가
        n = n+1 #n은 n+1
    else: #그렇지 않으면
        ptv = np.array([[x,y]]) #ptv는 배열
        n = 1 #n은 1
        p0 = p #p0는 p
    p1 = p #p1은 p

img0 = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE) #저장된 이미지 읽어오기
    
if img0 is None: #이미지가 없으면
    print('error') #error 출력
    img0 = np.random.random((512, 512)) * 255 #img0는 랜덤하게 출력된 화면
    img0 = np.uint8(img0) #정수형 자료형으로 데이터 형태 지정
img_r = np.random.random((512, 512)) * 255 #img_r은 랜덤하게 출력된 화면
img_r = np.uint8(img_r) #정수형 자료형으로 데이터 형태 지정
print('img0 :', img0.shape) #img0 : 출력
cv2.namedWindow('image-in', cv2.WINDOW_AUTOSIZE) #새로운 윈도우 창 이름 설정/autosize크기
cv2.imshow('image-in', img0) #저장된 이미지 보여주기

fun = 1
if fun == 1:
    cv2.setMouseCallback('image-in', onMouse) #마우스 이벤트가 발생했을 때 콜백 함수
# 키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()