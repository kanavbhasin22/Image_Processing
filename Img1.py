import cv2
import numpy
#img=cv2.imread('Microsoft.jpg',1)
img=numpy.zeros([1024,1024,3],numpy.uint8)

img=cv2.line(img,(0,0),(255,255),(200,100,125),10)
img=cv2.arrowedLine(img,(255,0),(255,255),(124,153,144),10)

img=cv2.rectangle(img,(333,0),(512,300),(233,244,250),10)
img=cv2.circle(img,(100,100),100,(255,0,0),10)

font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'Microsoft',(200,200),font,3,(255,255,0),5)

cv2.imshow('Image',img)
k=cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('imgcopy.jpg',img)
    cv2.destroyAllWindows()

