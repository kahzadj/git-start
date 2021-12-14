from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog
import sqlite3
import glob, os, os.path
import PIL.Image
from cv2 import cv2
import numpy as np

#_______________________________
root = Tk()
root.title('my first window')
root.directory = tkinter.filedialog.askdirectory()
source1 = os.path.join(root.directory,'*.jpg')
photos = glob.glob(source1)
root.geometry("1366x728")

# ----------resize photo-----------
def resize(nom):
	imag = PIL.Image.open(photos[nom])
	exif_data = imag._getexif()
	a = exif_data[40962]
	b = exif_data[40963]
	c = int(700*a/b)
	print (c)
	img = Image.open(photos[nom])
	new_img = img.resize((c,700))
	new_img.save("E:/exam projects/myproject/photo viwer/polo.jpg", "JPEG", optimize=True)

resize(0)
my_img = ImageTk.PhotoImage(Image.open('E:/exam projects/myproject/photo viwer/polo.jpg'))
my_label = Label(image=my_img)
my_label.grid(row=1, column=0,columnspan=3)

#_______________create next button________________
def next1(num):
	global photos
	global next_btn
	global previous_btn
	global my_img
	global img

	img = PIL.Image.open(photos[num-1])
	resize(num-1)
	my_img = ImageTk.PhotoImage(Image.open('E:/exam projects/myproject/photo viwer/polo.jpg'))
	my_label = Label(image=my_img)
	my_label.grid(row=1, column=0,columnspan=3)
	
	next_btn = Button(root, text="  Next  ", command=lambda: next1(num+1))
	previous_btn = Button(root, text="Previous", command=lambda: previous(num-1))
	
	if num == (len(photos)):
		next_btn = Button(root, text="  Next  ", state=DISABLED)
		next_btn.grid(row=1, column=2, ipadx=30)

	my_label.grid(row=1, column=0,columnspan=3)
	next_btn.grid(row=0, column=2, ipadx=30)
	previous_btn.grid(row=0, column=0, ipadx=30)

#_________________create previous button__________________
def previous(num):
	global photos
	global next_btn
	global previous_btn
	global my_img
	global img

	img = PIL.Image.open(photos[num-1])
	resize(num-1)
	my_img = ImageTk.PhotoImage(Image.open('E:/exam projects/myproject/photo viwer/polo.jpg'))
	my_label = Label(image=my_img)
	my_label.grid(row=1, column=0,columnspan=3)

	next_btn = Button(root, text="  Next  ", command=lambda: next1(num+1))
	previous_btn = Button(root, text="Previous", command=lambda: previous(num-1))
	
	if num == (1):
		previous_btn = Button(root, text="Previous", state=DISABLED)
		previous_btn.grid(row=1, column=2, ipadx=30)

	my_label.grid(row=1, column=0,columnspan=3)
	next_btn.grid(row=0, column=2, ipadx=30)
	previous_btn.grid(row=0, column=0, ipadx=30)

#_________________create button________________________
next_btn = Button(root, text="  Next  ", command= lambda: next1(2))
next_btn.grid(row=0, column=2, ipadx=30)

previous_btn = Button(root, text="Previous", command=previous)
previous_btn.grid(row=0, column=0, ipadx=28)

exit_btn = Button(root, text="Exit", command=root.quit)
exit_btn.grid(row=0, column=1, ipadx=30)

root.mainloop()
