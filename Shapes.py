import numpy
import cv2

img=cv2.imread('shapes.png')
img=cv2.resize(img,(512,512))
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, thresh=cv2.threshold(imgray,240,255,cv2.THRESH_BINARY)
contours,_= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],-1,(0,0,0),3)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx)==3:
        cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspect=float(w)/h
        print(aspect)
        if aspect >0.95 and aspect <1.05:
            cv2.putText(img,'Square',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        else:
            cv2.putText(img,'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    elif len(approx)==5:
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    else:
        cv2.putText(img,'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
cv2.imshow('Shapes',img)
cv2.waitKey()
cv2.destroyAllWindows()