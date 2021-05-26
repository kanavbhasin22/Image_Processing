import cv2
from matplotlib import pyplot
import numpy

img=cv2.imread('gradient.png',0)
_, th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_, th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_, th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_, th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_, th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

#titles=['Original','Binary','Inv Bnary','Trunc','ToZero','ToZero Inv']
#images=[img,th1,th2,th3,th4,th5]

#for i in range(6):
    #pyplot.subplot(2,3,i+1), pyplot.imshow(images[i],'gray')
    #pyplot.title(titles[i])
    #pyplot.xticks([]),pyplot.yticks([])

cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)
#pyplot.show()
cv2.waitKey()
cv2.destroyAllWindows()
