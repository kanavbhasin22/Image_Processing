import numpy
import cv2

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_FLAG_LBUTTON:

        #print(x,',',y)
        #font=cv2.FONT_HERSHEY_COMPLEX
        #strxy= str(x)+ ' , '+str(y)
        #cv2.putText(img,strxy,(x,y),font,1,(0,255,255),2,cv2.LINE_AA)
        #cv2.imshow('image',img)

        cv2.circle(img,(x,y),5,(0,255,255),2)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,255,255),5)
        cv2.imshow('image',img)

    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strbgr = str(blue) + ' , ' + str(green) + ' , ' + str(red)
        cv2.putText(img, strbgr, (x, y), font, 1, (0, 0,0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)

#img=numpy.zeros((512,512,3),numpy.uint8)
img=cv2.imread('Microsoft.jpg')
points=[]
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
