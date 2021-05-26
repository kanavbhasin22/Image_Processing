import cv2
import datetime

cap = cv2.VideoCapture(0)
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('Output.mp4',fourcc,20.0,(640,480))

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read()
    #
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==True:
        #out.write(frame)

        font=cv2.FONT_HERSHEY_COMPLEX
        text= 'Width: '+ str(cap.get(3)) +' Height: ' + str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(100,100),font,1,(0,255,255),2,cv2.LINE_AA)
        frame=cv2.line(frame,(100,100),(500,500),(125,125,125),10)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
cap.release()
#out.release()
cv2.destroyAllWindows()
