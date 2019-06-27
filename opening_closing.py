import cv2
import numpy as np

img = cv2.imread("letters.jpg")
ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("letters_closing.png",closing)
cv2.imwrite("letters_opening.png",opening)
