from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import glob, os, os.path
import PIL.Image
from cv2 import cv2
import numpy as np
i = 0
a = 0
def resize(nom):
	global photos
	img = Image.open(photos[nom])
	new_img = img.resize((1024,720))
	new_img.save("E:/exam projects/myproject/face of photo/polo.jpg", "JPEG", optimize=True)

photos = glob.glob('E:/exam projects/myproject/face of photo/sample/*.jpg')
for i in range(len(photos)):
	imagePath = (photos[i])
	cascPath = "C:/python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)
	i = i + 1

	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor = 1.3,
		minNeighbors = 4,
		minSize = (8, 8)
	)
	print("Found {0} faces!".format(len(faces)))
	# draw a rectzngle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		crop_img = image[y:y+h, x:x+w]
		#cv2.imshow("cropped", crop_img)
		a = a + 1
		status = cv2.imwrite('E:/exam projects/myproject/face of photo/ph{a}.jpg' ,crop_img)
		img = Image.open('E:/exam projects/myproject/face of photo/ph{a}.jpg')
		#new_img = img.resize((250,250))
		img.save("E:/exam projects/myproject/face of photo/face bank/face{0}.jpg".format(a) , "JPEG", optimize=True)
#cv2.imshow("Faces found", image)
cv2.waitKey(0)