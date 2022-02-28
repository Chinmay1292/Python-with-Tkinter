import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1600x900")
img = ImageTk.PhotoImage(Image.open("")) #Add file location here
img2 = ImageTk.PhotoImage(Image.open("")) #Add file2 location here
img3 = ImageTk.PhotoImage(Image.open("")) #Add file3 location here

l = Label()
l.pack()

x = 0
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image = img)
    elif x == 2:
        l.config(image = img2)
    elif x == 3:
        l.config(image=img3)
    x = x+1
    root.after(2000, move)

move()
root.mainloop()