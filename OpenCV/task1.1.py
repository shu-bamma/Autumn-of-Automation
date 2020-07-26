import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread("starry.jpg",0)
#cv.imshow("van gough",img)
#cv.waitKey(0)
#cv.destroyAllWindows()
plt.imshow(img,cmap="gray")
plt.show()
