import cv2 
import numpy as np
import  imutils
from matplotlib import pyplot as plt
img = cv2.imread('transform.png')
cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('2',res)#scaling 2 times
cv2.waitKey(0)
cv2.destroyAllWindows()

rows,cols = img[:,:,1].shape
M1 = np.float32([[1,0,-130],[0,1,-196]])#Translation matrix
M2 = np.float32([[1,0,120],[0,1,90]])
dst1 = cv2.warpAffine(img,M1,(cols,rows))
dst2 = cv2.warpAffine(img,M2,(cols,rows))
plt.subplot(121)
plt.imshow(dst1)
plt.subplot(122)
plt.imshow(dst2)
plt.show()

for angle in range(0,360,15):
	R=imutils.rotate_bound(img,angle)
	r=imutils.rotate(img,angle)
	cv2.imshow("nooob rotation",r)
	cv2.waitKey(0)
	cv2.imshow("pro rotation", R)
	cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur=cv2.blur(img,(5,5))#blurring the image
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.show()

pts1 = np.float32([[137,197],[201,202],[132,261],[202,267]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)#fixin perspective on the box
out = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(out),plt.title('Output')
plt.show()

#we can use diff methods for sharpenning our image...i found a kernel on wikipedia for the same....https://en.wikipedia.org/wiki/Kernel_(image_processing)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
im = cv2.filter2D(out, -1, kernel)
plt.subplot(121),plt.imshow(out),plt.title('Input')
plt.subplot(122),plt.imshow(im),plt.title('Output')
plt.show()



