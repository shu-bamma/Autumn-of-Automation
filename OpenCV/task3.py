import cv2 as cv
import  numpy as np
from matplotlib import pyplot as plt
cap=cv.VideoCapture(0)
while(cap.isOpened()):
	ret,frame=cap.read()
	if ret==True:
		gframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		laplacian = cv.Laplacian(gframe,cv.CV_64F)
		sobelx = cv.Sobel(gframe,cv.CV_64F,1,0,ksize=5)
		sobely = cv.Sobel(gframe,cv.CV_64F,0,1,ksize=5)

		cv.imshow("original",gframe)
		cv.imshow("laplacian",laplacian)
		cv.imshow("x",sobelx)
		cv.imshow("y",sobely)
		if cv.waitKey(25) & 0xFF==ord('c'):
			break
	else:
		break
cap.release()
cv.destroyAllWindows()
