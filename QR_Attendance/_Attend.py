import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64
import csv

from datetime import date, datetime
from tkinter.constants import GROOVE, RAISED, RIDGE
import tkinter as tk 
from tkinter import Frame, ttk, messagebox
from tkinter import *

# branch and Lecture input

window = tk.Tk()
window.title('Attendance System IT MU')
window.geometry('900x600') 
                          
year= tk.StringVar()      
branch= tk.StringVar()
sec= tk.StringVar() 
Lecture= tk.StringVar()

title = tk.Label(window,text="Attendance System IT MU",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=480,height=530)

ttk.Label(window, text = "Year",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=year,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4') 
combo_search.place(x=250,y=150)

ttk.Label(window, text = "Branch",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=200)
combo_search=ttk.Combobox(window,textvariable=branch,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=("CSE","ECE","CIVIL","IT","MECH","PHARMACY")
combo_search.place(x=250,y=200)

ttk.Label(window, text = "Section",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=250)
combo_search=ttk.Combobox(window,textvariable=sec,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('A','B','C','D')
combo_search.place(x=250,y=250)

ttk.Label(window, text = "Lecture",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=300)
combo_search=ttk.Combobox(window,textvariable=Lecture,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('CD','DAA','CN','Python','SS-III')
combo_search.place(x=250,y=300)

def checkk():
    if(year.get() and branch.get() and Lecture.get() and sec.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")

exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=380)



Manag_Frame=Frame(window,bg="lavender")
Manag_Frame.place(x=480,y=80,width=450,height=530)

canvas = Canvas(Manag_Frame, width = 300, height = 300,background="lavender")      
canvas.pack()      
img = PhotoImage(file="Bg.png")      
canvas.create_image(50,50, anchor=NW, image=img) 

window.mainloop()

# start webcam
cap=cv2.VideoCapture(0)
names=[]
today=date.today()
d= today.strftime("%b-%d-%Y")

# attendance file
fob=open(Lecture.get()+" "+branch.get()+"-"+sec.get()+" "+d+'.csv','w+',newline='')
lnwriter=csv.writer(fob)
# columns in file
lnwriter.writerow(["Enrollment No.","Class","Section","Year","Lecture","Intime"])

def enterData(z):   
    z=str(z)
    if z in names:
        pass
    else:
        it=datetime.now()
        names.append(z)
        z=''.join(str(z))
        intime = it.strftime("%H:%M:%S")
        # z.config(text=f"{decodedObjects[0].data.decode('ascii')}")
        print(z)
        lnwriter.writerow([z,branch.get(),sec.get(),year.get(),Lecture.get(),intime])
    return names 

print('Reading QR......')

#  check presence of data
def checkData(data):
    data=str(data)  
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'present marked')
        enterData(str(data))

while True:
    _, frame = cap.read()  #read from webcam
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
       
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1)&0xFF == ord('e'):
        cv2.destroyAllWindows()
        break
    
fob.close()