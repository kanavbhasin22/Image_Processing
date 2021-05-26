import cv2
import numpy

apple=cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
apppleorange=numpy.hstack((apple[:, :256],orange[:, 256:]))

#Image Pyramid for apple
apple_copy=apple.copy()
gp_apple=[apple_copy]
for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#Image Pyramid for Orange
orange_copy=orange.copy()
gp_orange=[orange_copy]
for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#Laplacian for apple
apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp_apple[i])
    laplacian=cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(laplacian)

#Laplacian for orange
orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp_orange[i])
    laplacian=cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)

#Add images
apple_orange_pyramid=[]
n=0
for apple_lap, orange_lap in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,ch= apple_lap.shape
    laplacian=numpy.hstack([apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]])
    apple_orange_pyramid.append(laplacian)

#Reconstruct
apple_orange_reconstruct= apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('appleorange',apppleorange)
cv2.imshow('Blended',apple_orange_reconstruct)
cv2.waitKey()
cv2.destroyAllWindows()