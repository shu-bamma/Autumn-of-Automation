import cv2 as cv
import  numpy as np
from matplotlib import pyplot as plt
cap = cv.VideoCapture(0) #0 is for my webcam

if (cap.isOpened()==False):
	print("error opening cameeeeeera")
while(cap.isOpened()):
	ret, frame=cap.read() #capture frame by frame
	if ret==True:
		gframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		(thresh, bwframe) = cv.threshold(gframe, 127, 255, cv.THRESH_BINARY)
		cv.imshow("original frame",frame)#show the current frame
		cv.imshow("in black and white",bwframe)
		#press a key on keyboard to exit
		if cv.waitKey(25) & 0xFF==ord('c'):
			break
	else:
		break
cap.release()#release the capture button after everything
cv.destroyAllWindows()
