#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="#262626")

#root.geometry("300x300")

def function1():
    
    os.system("python vehicle_detection_IP.py")

def function6():

    root.destroy()

#stting title for the window
root.title("Detections")

#creating a text label
Label(root, text="Vechicle Detection Using Haar Cascades",font=("arial",20),fg="white",bg="black",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="CAR DETECTION",font=("calibri",20),bg="#000000",fg='green',command=function1).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Exit",font=('calibri',20),bg="black",fg="red",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
