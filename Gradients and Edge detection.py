import cv2
import numpy
from matplotlib import pyplot

img=cv2.imread('Temple.jpg',0)
img=cv2.resize(img,(640,480))

lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=numpy.uint8(numpy.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobelx=numpy.uint8(numpy.absolute(sobelx))
sobely=numpy.uint8(numpy.absolute((sobely)))
sobelcombine=cv2.bitwise_or(sobelx,sobely)
edges=cv2.Canny(img,100,200)

titles=['img','lap','sobelx','sobely','sobelcombine','Canny']
images=[img,lap,sobelx,sobely,sobelcombine,edges]

for i in range(6):
    pyplot.subplot(2,3,i+1), pyplot.imshow(images[i],'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])
pyplot.show()