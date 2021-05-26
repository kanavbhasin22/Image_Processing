import numpy
import cv2
from matplotlib import pyplot

#img=numpy.zeros((200,200),numpy.uint8)
#cv2.rectangle(img,(0,100),(200,200),(255,255,255),-1)
img=cv2.imread('Temple.jpg')
img=cv2.resize(img,(512,512))

b,g,r=cv2.split(img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

pyplot.hist(b.ravel(),256,[0,256])
pyplot.hist(g.ravel(),256,[0,256])
pyplot.hist(r.ravel(),256,[0,256])
#pyplot.hist(img.ravel(),256,[0,256])

cv2.imshow('img',img)
pyplot.show()

cv2.waitKey()
cv2.destroyAllWindows()
