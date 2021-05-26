import cv2
import numpy

img=cv2.imread('Rocks.jpg',1)
img=cv2.resize(img,(512,512))

layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)
layer=gp[5]
cv2.imshow('Upper Level Gaussian',layer)
lp=[layer]

for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)

#lr1=cv2.pyrDown(img)
#lr2=cv2.pyrDown(lr1)
#ur1=cv2.pyrUp(img)
#ur2=cv2.pyrUp(ur1)

cv2.imshow('image',img)
#cv2.imshow('lr1',lr1)
#cv2.imshow('lr2',lr2)
#cv2.imshow('ur1',ur1)
#cv2.imshow('ur2',ur2)

cv2.waitKey()
cv2.destroyAllWindows()