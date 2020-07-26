import numpy as np
import matplotlib.pyplot as plt
import cv2

capture = cv2.VideoCapture("LionelMessi.mp4")
 
while(True):
    ret, frame = capture.read()
    img_bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(img_bw,252,255,0)
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for ct in contours:
        epsilon = 0.001*cv2.arcLength(ct,True)
        approx = cv2.approxPolyDP(ct,epsilon,True)
        cv2.drawContours(img_bw, [approx], 0, (0,0,0), 3)
        x = approx.ravel()[0]
        y=approx.ravel()[1]
        if len(approx)>15:
            cv2.putText(img_bw, "football", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0))
    cv2.imshow('video', img_bw)
     
    if cv2.waitKey(25) & 0xFF == ord('c'):
        break
 
capture.release()
cv2.destroyAllWindows()