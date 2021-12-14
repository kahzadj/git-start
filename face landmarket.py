from cv2 import cv2
import dlib
import numpy as np
cap = cv2.VideoCapture(0)

predictor = dlib.shape_predictor('C:/Python38/Lib/site-packages/cv2/data/shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x1 = face.left()    
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        #cv2.rectangle(frame, (x1,y1), (x2, y2), (90, 110, 255),3)
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x,y), 2, (110, 170, 110), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break 