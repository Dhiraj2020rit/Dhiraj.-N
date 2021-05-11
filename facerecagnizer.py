import cv2
face_data=cv2.CascadeClassifier("facrrecognizertool.xml")
webcam=cv2.VideoCapture(0)
while 1:
    work,video=webcam.read()
    reels=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY) 
    face=face_data.detectMultiScale(reels)
    for (x,y,w,h) in face:
        cv2.rectangle(video,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("My app",video) 
    key=cv2.waitKey(1)
    if key==27:
        break
