import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#show all video properties
for i in range(19):
    print (i, cap.get(i))

cap.set(30,160) #set width
cap.set(40,120) #set height
    
while(cap.isOpened()):
    ret, frame = cap.read()
    try:
        cv2.imshow('Frame',frame)
    except:
        print('EOF')
        break

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
