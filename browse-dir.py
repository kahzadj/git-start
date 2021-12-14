from tkinter import *
import tkinter.filedialog
root = Tk()
root.directory = tkinter.filedialog.askdirectory()
print (root.directory)