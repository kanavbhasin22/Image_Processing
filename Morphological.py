import cv2
from matplotlib import pyplot
import numpy

img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_, mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel=numpy.ones((5,5),numpy.uint8)
dilation=cv2.dilate(mask,kernel,iterations=3)
erosion=cv2.erode(mask,kernel,iterations=3)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)

titles=['Image','Mask','Dilation','Erosion','opening','closing','mg','th']
images=[img,mask,dilation,erosion,opening,closing,mg,th]
for i in range(8):
    pyplot.subplot(2,4,i+1), pyplot.imshow(images[i],'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])

pyplot.show()