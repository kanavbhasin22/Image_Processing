import cv2
import numpy

img=cv2.imread('smarties.png')
output=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
circle=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=40,minRadius=0,maxRadius=0)

detected= numpy.uint16(numpy.around(circle))
for (x,y,r) in detected [0,:]:
    cv2.circle(output,(x,y),r,(132,68,120),2)
    cv2.circle(output,(x,y),2,(255,0,0),2)

cv2.imshow('output',output)
cv2.waitKey()
cv2.destroyAllWindows()