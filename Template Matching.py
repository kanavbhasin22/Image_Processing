import cv2
import numpy

img=cv2.imread('messi5.jpg')
#img=cv2.resize(img,(512,512))
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template=cv2.imread('Messi_Template.PNG',0)
#template=cv2.resize(template,(300,300))

w,h=template.shape[::-1]

res=cv2.matchTemplate(grayimg,template,cv2.TM_CCOEFF_NORMED)
print(res)
threshold=0.99;
loc=numpy.where(res>=threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()