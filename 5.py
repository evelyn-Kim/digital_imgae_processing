import cv2

# 트랙바가 조금이라도 움직이면 출력(다음 문구)
def onZoom(val):
    global cap
    cap.set (cv2.CAP_PROP_ZOOM, val) # 설정/캠제어
    
def onFocus(val):
    global cap
    cap.set (cv2.CAP_PROP_FOCUS, val) # 설정/캠제어
    
def put_string(frame, text, val, pt, color=(120, 200, 90)):
    text += str(val)
    shade = (pt[0]+2, pt[1]+2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText (frame, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText (frame, text, pt, font, 0.7, color, 2)
    
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0) # 자동 초점 중지
cap.set(cv2.CAP_PROP_BRIGHTNESS, 100) # 밝기 초기화
cap.set(cv2.CAP_PROP_ZOOM, 1) # digital zoom – 1배
frame_rate = cap.get(cv2.CAP_PROP_FPS)

title = "video" 
cv2.namedWindow (title)
cv2.createTrackbar ('zoombar', title, 0, 10, onZoom)
cv2.createTrackbar ('focusbar', title, 0, 40, onFocus)

while True :
    ret, frame = cap.read()
    
    if not ret: 
        break #오작동?
    if cv2.waitKey(30) >= 0: 
        break #끄기
        
    zval = int(cap.get(cv2.CAP_PROP_ZOOM))
    fval = int(cap.get(cv2.CAP_PROP_FOCUS))
    
    put_string (frame, 'zoom : ', zval, (10, 240))
    put_string (frame, 'focus : ', fval, (10, 270))
    cv2.imshow(title, frame)
cap.release()