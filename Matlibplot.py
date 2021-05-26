import cv2
from matplotlib import pyplot

img=cv2.imread('Microsoft.jpg', 1)
img=cv2.resize(img,(512,512))
cv2.imshow('image',img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

pyplot.imshow(img)
pyplot.xticks([]),pyplot.yticks([])
pyplot.show()

cv2.waitKey()
cv2.destroyAllWindows()