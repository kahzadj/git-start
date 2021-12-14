from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.filedialog
import glob, os, os.path ,subprocess
import PIL.Image
import shutil
import tkinter as tk
from tkinter import messagebox

#___________create button & label_________________________
root = Tk()
global source1
global source2
source1 = None
source2 = None

root.title('Manager Of Photo by Date')
#root.iconbitmap(":/exe/icon.ico")
root.geometry("600x370")

text_label = Label(root, text="Select The Photos Folder:", font=('Cambria', '10', ""), fg="black")
text_label.grid(row=1, column=0, pady=10, ipadx=6)

address_text1 =Text (root, height=1, width=30 )
address_text1.grid(row=1, column=1, columnspan=3, ipadx=40)

source_btn = Button(root, text="Browse", command= lambda: first())
source_btn.grid(row=1, column=4,  padx=5, ipadx=15)

text_label = Label(root, text="Select The Target Folder:", font=('Cambria', '10', ""), fg="black")
text_label.grid(row=2, column=0, ipadx=6)

address_text2 =Text (root, height=1 , width=30 )
address_text2.grid(row=2, column=1, columnspan=3, ipadx=40)

target_btn = Button(root, text="Browse", command= lambda: target())
target_btn.grid(row=2, column=4, ipadx=15)

var4 = IntVar()
chekbtm_year=Checkbutton(root, text="Sort By Years. ",font=('Cambria', '10', ""), variable=var4)
chekbtm_year.grid(row=5, column=1, columnspan=3, pady=5, sticky=W)
year = var4.get()

var3 = IntVar()
chekbtm_month=Checkbutton(root, text="Sort By Months.",font=('Cambria', '10', ""), variable=var3)
chekbtm_month.grid(row=4, column=1, columnspan=3, sticky=W)
month = var3.get()

var2 = IntVar()
chekbtm_day=Checkbutton(root, text="Sort By Days.  ",font=('Cambria', '10', ""), variable=var2)
chekbtm_day.select()
chekbtm_day.grid(row=3, column=1, columnspan=3, pady=5, sticky=W)
day = var2.get()

space_label = Label(root, text="_____________________________________________________", font=('Cambria', '12', ""), fg="black")
space_label.grid(row=6, column=1, columnspan=3, ipadx=5)

var1 = IntVar()
chekbtm_del=Checkbutton(root, text="Delete old photos after copying.",font=('Cambria', '10', ""), variable=var1)
chekbtm_del.grid(row=7, column=1, columnspan=3, sticky=W)

Run_btn = Button(root, text=" Run " , state=DISABLED , command= lambda: done())
Run_btn.grid(row=10, column=1, pady=10, padx=5, ipadx=50)

stop_btn = Button(root, text=" Stop ", command= lambda: root.quit())
stop_btn.grid(row=10, column=2, pady=10, ipadx=20)

close_btn = Button(root, text="Close ", command= lambda: root.quit())
close_btn.grid(row=10, column=3, pady=10, padx=5, ipadx=20)

text_label = Label(root, text="percent of progress!", font=('Cambria', '10', ""), fg="black")
text_label.grid(row=8, column=1, columnspan=3, pady=10, ipadx=6)

progress = Progressbar(root, orient = HORIZONTAL, length = 300)
progress.grid(row=9, column=1, columnspan=3, ipadx=10 )
progress['value'] = 0
root.update_idletasks()

#______________create source button_______________
def first():
    global photos
    global source1
    global source2
    global num
    global var1
    root.directory1 = tkinter.filedialog.askdirectory()
    source1 = os.path.join(root.directory1,'*.jpg')
    photos = glob.glob(source1)
    address_text1 =Text (root, height=1, width=30 )
    address_text1.grid(row=1, column=1, columnspan=3, ipadx=40)
    address_text1.insert(INSERT, root.directory1)
    num = 0
    if (source1 != None and source2 != None and (day == 1 or month == 1 or year == 1)):
        Run_btn = Button(root, text=" Run " , command= lambda: done())
        Run_btn.grid(row=10, column=1, pady=10, padx=5, ipadx=50)

#_____________create target button_______________
def target():
    global photos
    global num
    global source1
    global source2 
    root.directory2 = tkinter.filedialog.askdirectory()
    source2 = root.directory2
    address_text2 =Text (root, height=1 , width=30 )
    address_text2.grid(row=2, column=1, columnspan=3, ipadx=40)
    address_text2.insert(INSERT, root.directory2)
    num=0

    if (source1 != None and source2 != None and (day == 1 or month == 1 or year == 1)):
        Run_btn = Button(root, text=" Run " , command= lambda: done())
        Run_btn.grid(row=10, column=1, pady=10, padx=5, ipadx=50)
   
#________create next button__________
def done():
    global num
    global photos
    global source2
    global source1
    global delete
    num = 0
    
    chekbtm_year=Checkbutton(root, text="Sort By Years. ",font=('Cambria', '10', ""), variable=var4)
    chekbtm_year.grid(row=5, column=1, columnspan=3, pady=5, sticky=W)
    year = var4.get()

    chekbtm_month=Checkbutton(root, text="Sort By Months.",font=('Cambria', '10', ""), variable=var3)
    chekbtm_month.grid(row=4, column=1, columnspan=3, sticky=W)
    month = var3.get()

    chekbtm_day=Checkbutton(root, text="Sort By Days.  ",font=('Cambria', '10', ""), variable=var2)
    chekbtm_day.grid(row=3, column=1, columnspan=3, pady=5, sticky=W)
    day = var2.get()

    chekbtm_del=Checkbutton(root, text="Delete old photos after copying.",font=('Cambria', '10', ""), variable=var1)
    chekbtm_del.grid(row=7, column=1, columnspan=3, sticky=W)
    delete = var1.get()

    progress = Progressbar(root, orient = HORIZONTAL, length = 300)
    progress.grid(row=9, column=1, columnspan=3, ipadx=10 )
    messagebox.showinfo("info!","there are {:g} photo in this folder!".format(len(photos)))

    while num < len(photos):
        img = PIL.Image.open(photos[num])
        exif_data = img._getexif()
        text_label = Label(root, text='{:g} %'.format(int((100/len(photos))*num)) , font=('Cambria', '10', ""), fg="black")
        text_label.grid(row=9, column=4, ipadx=6)

        if exif_data == None:
            point = os.path.join(source2,'Other')
            if not os.path.exists(point):
                os.makedirs(point)
            name = str (photos[num])
            shutil.copy(name, point)            
            progress['value'] = (100/len(photos))*num
            root.update_idletasks()
            num += 1
        elif  not ((exif_data.get(36867)) == None):
            a = str(exif_data[36867])
            day1 = a[0:10]
            year1 = a[0:4]
            month1 = a[0:7]
            day2 = day1.replace(':', '-')
            month2 = month1.replace(':', '-')
            d = str(source2)
            if year == 1 :
                directory_year = os.path.join(d,year1)
                if not os.path.exists(directory_year):
                    os.makedirs(directory_year)
                if month == 1:
                    dy = str(directory_year)
                    directory_month = os.path.join(dy,month2)
                    if not os.path.exists(directory_month):
                        os.makedirs(directory_month)
                    if day == 1:
                        dd = str(directory_month)
                        directory_day = os.path.join(dd,day2)
                        if not os.path.exists(directory_day):
                            os.makedirs(directory_day)
                        name = str (photos[num])
                        shutil.copy(name, directory_day)
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks()
                        num += 1

                    else:
                        name = str (photos[num])
                        shutil.copy(name, directory_month)
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks()
                        num += 1
                    
                else:
                    if day == 1:
                        dd = str(directory_year)
                        directory_day = os.path.join(dd,day2)
                        if not os.path.exists(directory_day):
                            os.makedirs(directory_day)
                        name = str (photos[num])
                        shutil.copy(name, directory_day)
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks()
                        num += 1

                    else:
                        name = str (photos[num])
                        shutil.copy(name, directory_year)                        
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks()
                        num +=1
            else:
                if month == 1:
                    directory_month = os.path.join(d,month2)
                    if not os.path.exists(directory_month):
                        os.makedirs(directory_month)
                    if day == 1:
                        dd = str(directory_month)
                        directory_day = os.path.join(dd,day2)
                        if not os.path.exists(directory_day):
                            os.makedirs(directory_day)
                        name = str (photos[num])
                        shutil.copy(name, directory_day)
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks()
                        num +=1
                    else:
                        name = str (photos[num])
                        shutil.copy(name, directory_month)
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks()
                        num += 1
                else:
                    if day == 1:
                        directory_day = os.path.join(d,day2)
                        if not os.path.exists(directory_day):
                            os.makedirs(directory_day)
                        name = str (photos[num])
                        shutil.copy(name, directory_day)
                        progress['value'] = (100/len(photos))*num
                        root.update_idletasks() 
                        num += 1

                    else:
                        messagebox.showwarning("Warning!","Select The directory items!")
                        break

        else:
            point = os.path.join(source2,'Other')
            if not os.path.exists(point):
                os.makedirs(point)
            name = str (photos[num])
            shutil.copy(name, point)           
            num += 1
            progress['value'] = (100/len(photos))*num
            root.update_idletasks() 
    
    if delete == 1:
        num = 0
        img = PIL.Image.open("D:/photo manager/aaa.jpg")
        while num < len(photos):
            dele = str (photos[num])
            os.remove(dele)    
            num +=1

    if num == len(photos):
        progress['value'] = 100
        root.update_idletasks()
        text_label = Label(root, text='100%' , font=('Cambria', '10', ""), fg="black")
        text_label.grid(row=9, column=4, ipadx=6)
        yes=messagebox.askyesno("congratulations","process successfully completed. \nWould you like to open the result folder?",)
        if yes == True:
            subprocess.run(['explorer', os.path.realpath(source2)])
root.mainloop()