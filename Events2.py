import numpy
import cv2

def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        cv2.circle(img,(x,y),5,(255,0,0),5)

        mycolorimage=numpy.zeros((512,512,3),numpy.uint8)
        mycolorimage[:]=[blue,green,red]

        cv2.imshow('image',mycolorimage)

img=cv2.imread('Microsoft.jpg')
cv2.imshow('image',img)
points=[]

cv2.setMouseCallback('image',click_event)

cv2.waitKey()
cv2.destroyAllWindows()