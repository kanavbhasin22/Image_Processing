import cv2
import numpy

img=cv2.imread('chessboard.png')
img=cv2.resize(img,(512,512))
cv2.imshow('img',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=numpy.float32(gray)
dst=cv2.cornerHarris(gray,2,3,0.03)

dst=cv2.dilate(dst,None)
img[dst > 0.01*dst.max()]=[255,0,0]

cv2.imshow('dst',img)
cv2.waitKey()
cv2.destroyAllWindows()
