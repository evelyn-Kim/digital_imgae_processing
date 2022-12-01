import cv2
import numpy as np

p1 = (-1, -1) #p1 지정
red = (0, 0, 255) #red 색 지정

def onMouse():
    p = []  #클릭한 포인트 저장
    mask_list = []  #마스크 리스트 저장

    #마스크 추출을 위한 마우스 클릭 이벤트 정의
    def drawMask(event, x, y, flags, par):
        global point, c
        img0 = img.copy()

        if event == cv2.EVENT_LBUTTONDOWN:  #색은 red / 마우스 왼쪽 버튼 클릭 시 point에 (x,y)좌표를 추가 및 리스트에 추가
            c = red
            point.append((x, y))
            mask_list.append(point)

        elif event == cv2.EVENT_RBUTTONDOWN: #마우스 오른쪽 버튼 클릭 시 출력
            result = np.zeros(img.shape, np.uint8)  #최종 마스크 이미지(행렬)

            for point in mask_list: #리스트에서 포인트 반복문
                if not point: #포인트가 없으면 그대로 진행
                    continue
                mask = np.zeros(img.shape, np.uint8)
                points = np.array(point, np.int32)
                points = points.reshape((-1, 1, 2)) #mask_list 2차원을 이미지와 동일하게 3차원으로 재배열
                mask = cv2.polylines(mask, [points], True, (255, 255, 255), 2) #포인트를 연결하는 라인을 설정 후 마스크 생성
                mask2 = cv2.fillPoly(mask.copy(), [points], (255, 255, 255)) #채워진 다각형 마스크 생성

                cv2.imshow('image-out', cv2.bitwise_and(mask2, img)) #img와 mask2에 중첩된 부분을 추출 및 보여주기

                result = cv2.add(result, cv2.bitwise_and(mask2, img)) #마스크 이미지끼리 더하기

        try:
            if len(point) > 0: #마우스 포인트 원으로 지정
                cv2.circle(img0, point[-1], 2, (0, 0, 255), -1)
        except:
            point = []

        if len(point) > 1: #마우스 포인트 연결 라인 생성
            for i in range(len(point) - 1):
                cv2.circle(img0, point[i], 5, (0, 0, 255), -1)
                cv2.line(img=img0, pt1=point[i], pt2=point[i + 1], color = red, thickness=2)

        if len(mask_list) > 0: #마스크 여러 개일때 포인트 연결 라인 생성
            for m in mask_list:
                for i in range(len(m) - 1):
                    cv2.circle(img0, m[i], 5, (0, 0, 255), -1)
                    cv2.line(img=img0, pt1=m[i], pt2=m[i + 1], color = red, thickness=2)

        cv2.imshow('image', img0) #이미지 화면 출력

    img = cv2.imread('mung.png') #저장된 이미지 읽어 오기
    if img is None: #이미지가 없으면
        print('error') #error 출력
    cv2.namedWindow('image') #새로운 윈도우 창 이름 설정
    cv2.setMouseCallback('image', drawMask) #마우스 이벤트가 발생했을 때 콜백 함수
    
key = 1 #key 지정
if key == 1: onMouse()
# 키 입력 대기 시간으로 입력이 없으면 종료하는데, 0 이면 무한대기
cv2.waitKey(0)
cv2.destroyAllWindows()