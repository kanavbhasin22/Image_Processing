import cv2
import numpy

cap = cv2.VideoCapture(0)
ret, frame=cap.read()
ret, frame1= cap.read()
ret, frame2= cap.read()
while (cap.isOpened()):
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _, thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilation=cv2.dilate(thresh,None,iterations=10)
    countours,_=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    for countour in countours:
        (x,y,w,h)=cv2.boundingRect(countour)
        if cv2.contourArea(countour) < 5000:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,'Status: '.format('Movement'),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
    #cv2.drawContours(frame1,countours,-1,(0,255,0),1)

    if ret==True:
        cv2.imshow('Video',frame)
        cv2.imshow('Contours',frame1)
        frame1=frame2
        ret,frame2=cap.read()
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
