import cv2
import numpy

img=cv2.imread('Microsoft.jpg')
img=cv2.resize(img,(512,512))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,50,150,apertureSize=3)
cv2.imshow('edge',edge)
lines=cv2.HoughLinesP(edge,1,numpy.pi/180,100,minLineLength=10,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,0),2)

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()