import cv2
import numpy
from matplotlib import pyplot

img=cv2.imread('Microsoft.jpg', 1)
img=cv2.resize(img,(640,480))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel=numpy.ones((5,5),numpy.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0) #Best among all
median=cv2.medianBlur(img,5)  #Salt and pepper noise
bilateral=cv2.bilateralFilter(img,5,75,75)

images=[img,dst,blur,gblur,median,bilateral]
titles=['img','2D Convolution','blur','gblur','median','bilateral']

for i in range(6):
    pyplot.subplot(2,3,i+1), pyplot.imshow(images[i])
    pyplot.title(titles[i])
    pyplot.xticks([]),pyplot.yticks([])
pyplot.show()