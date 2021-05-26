import cv2
import numpy

img=cv2.imread('Microsoft.jpg',1)
img=cv2.resize(img,(640,480))
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(imggray,100,255,0)
countours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours: "+ str(len(countours)))

cv2.drawContours(img,countours,-1,(0,0,0),1)

cv2.imshow('Image',img)
cv2.imshow('Gray image',imggr`ay)
cv2.waitKey()
cv2.destroyAllWindows()