import numpy
import cv2

img1=numpy.zeros((512,1024,3),numpy.uint8)
img1=cv2.rectangle(img1,(512,512),(1024,0),(255,255,255),-1)

img2=numpy.zeros((512,1024,3),numpy.uint8)
img2=cv2.rectangle(img2,(200,0),(800,200),(255,255,255),-1)

bitand=cv2.bitwise_and(img1,img2)
bitor=cv2.bitwise_or(img1,img2)
bitxor=cv2.bitwise_xor(img1,img2)
bitnot1=cv2.bitwise_not(img1)
bitnot2=cv2.bitwise_not((img2))

cv2.imshow('bitand',bitand)
cv2.imshow('bitor',bitor)
cv2.imshow('bitxor',bitxor)
cv2.imshow('bitnot1',bitnot1)
cv2.imshow('bitnot2',bitnot2)

cv2.waitKey()
cv2.destroyAllWindows()