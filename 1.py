import numpy as np
import cv2

image0 = np.zeros((200,400), np.uint8)
image0[:]=100
image1 = np.zeros((200,400), np.uint8)
image1.fill(255)

wtitle1, wtitle2 = 'Position1', 'Position2'

cv2.namedWindow(wtitle1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(wtitle2)

cv2.imshow(wtitle1, image0)
cv2.imshow(wtitle2, image1)
cv2.waitKey(0)
cv2.destroyAllWindows()