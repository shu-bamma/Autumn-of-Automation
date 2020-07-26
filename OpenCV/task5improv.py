import cv2
import numpy as np
from matplotlib import pyplot as plt

COUNT_MIN = 2
capture = cv2.VideoCapture("LionelMessi.mp4")
while(True):
    ret, frame = capture.read()
    im=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('.\img2.jpg',im)
    img1 = cv2.imread('foot_query.jpg',0)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    try:
        matches = flann.knnMatch(des1,des2,k=2)
    except:
        continue
    cool = []
    for m,n in matches:
        if m.distance < 0.5*n.distance:
            cool.append(m)
    if len(cool)>COUNT_MIN:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in cool ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in cool ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
        print("Not enough matches are found - %d/%d" % (len(cool),COUNT_MIN))
        matchesMask = None
    draw_params = dict(matchColor = (0,255,0),singlePointColor = None,matchesMask = matchesMask,flags = 2)

    img3 = cv2.drawMatches(img1,kp1,img2,kp2,cool,None,**draw_params)
    cv2.imshow('video', img3)
    if cv2.waitKey(10) & 0xFF == ord('c'):
        break
 
capture.release()
cv2.destroyAllWindows()