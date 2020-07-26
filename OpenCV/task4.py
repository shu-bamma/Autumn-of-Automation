import cv2 
import  numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('shapes.jpg',cv2.IMREAD_GRAYSCALE)
a,thresh=cv2.threshold(img,230,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
	approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)#the last true is for it to be closed
	cv2.drawContours(img,[approx],-1,(0,255,0),2)
	x = approx.ravel()[0]
	y = approx.ravel()[1]
	if len(approx)==3:
		cv2.putText(img,"triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
	elif len(approx)==4:
		x1,y1,w,h=cv2.boundingRect(approx)
    	aspectRatio=float(w)/h
    	print(aspectRatio)
    	if aspectRatio>=0.95 and aspectRatio<=1.05:
    		cv2.putText(img,"square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    	else:
    		cv2.putText(img,"rectagle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))




cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



