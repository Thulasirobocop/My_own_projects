import cv2 
import numpy as np
url = 'http://192.168.1.2:8080/video'
cap = cv2.VideoCapture(url)
vid = cv2.VideoCapture(0)
#vid_cod = cv2.VideoWriter_fourcc(*'XVID')
while(True):
    ret, frame = cap.read()
    ret1, frame1 = vid.read()
    frame=cv2.resize(frame,(720,600))
    frame1=cv2.resize(frame1,(720,600))
    both = np.concatenate((frame, frame1), axis=1)
    cv2.imshow('Both',both)
    #cv2.imshow('frame',frame)
    #cv2.imshow('frame1',frame1)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()
