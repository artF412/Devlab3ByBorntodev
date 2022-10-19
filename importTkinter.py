from cProfile import label
from tkinter import *
#from tkinter import * // เป็นคำสั่งในการเรียนใช้งานทุก Module
#import tkinter // เป็นคำสั่งเรียกใช้งานแต่ต้องใส่คำสั่งที่อยากใช้ลงไปด้วย

def sayMyName():
    print("Chalantorn Supprasert")

mainWindow = Tk()
buttonClike = Button(mainWindow,text="Clike Me1",command = sayMyName,width=20,height=10)
buttonClike.place(x=70,y=20)
buttonClike2 = Button(mainWindow,text="Clike Me2",command = sayMyName).grid(row=0,column=0)
label1 = Label(mainWindow,text="Hello My Name Is",width=30,height=10,fg="purple",bg="#93FF49",font=("Cascadia Code",8),anchor="w")
label1.place(x=20,y=200)
mainWindow.mainloop()