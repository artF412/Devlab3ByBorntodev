from re import L
from tkinter import *

def leftClikeButton(event):
    print("Left Clike !!")

def doubleClikeButton(event):
    print("Double Clike !!")

main = Tk()
Button1 = Button(main,text="My Button !!")
Button1.pack()
Button1.bind('<Button-1>',leftClikeButton)
Button1.bind('<Double-1>',doubleClikeButton)
main.mainloop()