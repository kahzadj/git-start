from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog
import sqlite3
import glob, os, os.path
import PIL.Image
import dlib
from cv2 import cv2
import numpy as np
import face_recognition

#______________________________________________________________

kahzad_image = face_recognition.load_image_file('E:/exam projects/main project/kahzad.jpg')
kahzad_face_encoding = face_recognition.face_encodings(kahzad_image)[0]

azin_image = face_recognition.load_image_file('E:/exam projects/main project/azin.jpg')
azin_face_encoding = face_recognition.face_encodings(azin_image)[0]

azadeh_image = face_recognition.load_image_file("E:/exam projects/main project/azadeh.jpg")
azadeh_face_encoding = face_recognition.face_encodings(azadeh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    kahzad_face_encoding,
    azadeh_face_encoding,
    azin_face_encoding
]
known_face_names = [
    "kahzad",
    "azadeh",
    "azin"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
#______________________________________________________________
a = 0
i = 0

predictor = dlib.shape_predictor('C:/Python38/Lib/site-packages/cv2/data/shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()
#_______________________________
root = Tk()
root.title('my first window')
root.directory = tkinter.filedialog.askdirectory()
source1 = os.path.join(root.directory,'*.jpg')
photos = glob.glob(source1)

for photo in photos:
    imagePath = (photos[i])
    frame = cv2.imread(imagePath)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    i += 1
    print("Found {0} faces!".format(len(faces)))
    
    for face in faces:
        face_imag = cv2.cvtColor(face,cv2.COLOR_GRAY2RGB)

        matches = face_recognition.compare_faces(known_face_encodings, facse)
        name = "Unknown"
        
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1,y1), (x2, y2), (90, 110, 255),3)
        crop_img = frame[y1:y2, x1:x2]
        a += 1
        status = cv2.imwrite('ph{a}.jpg' ,crop_img)
        img = Image.open('ph{a}.jpg')
        img.save("E:/exam projects/main project/face bank/face{0}.jpg".format(a) , "JPEG", optimize=True)




root.mainloop()
