from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog
import glob, os, os.path
import PIL.Image
from cv2 import cv2

#_______________________________
root = Tk()
root.title('my first window')
root.directory = tkinter.filedialog.askdirectory()
source1 = os.path.join(root.directory,'*.jpg')
photos = glob.glob(source1)
root.geometry("1366x728")
i = 1
for photo in photos:
    imag = PIL.Image.open(photo)
    exif_data = imag._getexif()
    a = exif_data[40962]
    b = exif_data[40963]
    c = int(700*a/b)
    print (c)
    img = Image.open(photo)
    new_img = img.resize((c,700))
    new_img.save("E:/exam projects/main project/source/photo{0}.jpg".format(i), "JPEG", optimize=True)
    i += 1