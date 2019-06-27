import numpy as np
import cv2

cap = cv2.VideoCapture('peopleCounter.avi') #Open video file

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) #Create the background substractor

while(cap.isOpened()):
    ret, frame = cap.read() #read a frame
    
    fgmask = fgbg.apply(frame) #Use the substractor
    
    try:        
        cv2.imshow('Frame',frame)
    
        cv2.imshow('Background Substraction',fgmask)
        ret, thresh1 = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        kernel = np.ones((5,5),np.uint8)
        fg = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
        fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, kernel)
        
        cv2.imshow('opening closing',fg)
    except:
        #if there are no more frames to show...
        print('EOF')
        break
    
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows
