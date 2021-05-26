import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#img=cv2.imread('Face.jpg')
#img=cv2.resize(img,(700,700))

cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,img=cap.read()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roigray=gray[y:y+h,x:x+w]
        roicolor=img[y:y+h,x:x+w]
        eyes=eyes_cascade.detectMultiScale(roigray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roicolor,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
