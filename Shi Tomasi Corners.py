import cv2
import numpy

img=cv2.imread('Microsoft.jpg')
img=cv2.resize(img,(512,512))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,1000,0.01,10)
corners=numpy.int0(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,(0,0,0),-1)
print(len(corners))
cv2.imshow('dst',img)
cv2.waitKey()
cv2.destroyAllWindows()