import cv2
import numpy as np
#https://github.com/Itseez/opencv/tree/master/data/haarcascades
#REAL TIME FACE DETECTION
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#xml file has a data of many coords of images and without images
videocapture=cv2.VideoCapture(0)
scale_factor=1.3
while 1:
    ret,pic=videocapture.read()
    faces= face_cascade.detectMultiScale(pic,scale_factor,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'ME',(x,y),font,2,(255,35,255),2,cv2.LINE_AA)
    print("Number of faces found {}".format(len(faces)))
    cv2.imshow('face',pic)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cv2.destroyAllWindows()
#image face detection
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pic=cv2.imread('test.jpg')
scale_factor=1.3
while 1:
    faces= face_cascade.detectMultiScale(pic,scale_factor,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'ME',(x,y),font,2,(255,35,255),2,cv2.LINE_AA)
    print("Number of faces found {}".format(len(faces)))
    cv2.imshow('face',pic)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cv2.destroyAllWindows()
