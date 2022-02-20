import random
from tkinter import *
from PIL import Image, ImageTk 

root = Tk()
root.title("TechnoLord Programming")
root.geometry("500x400")

l = Label(root, text="Roll Dice", font=("Helvetica 18 bold"), fg="Red")
l.pack()

#load 1
load = Image.open("Dice Images\\dice1.jpg")
load = load.resize((200, 200))
one = ImageTk.PhotoImage(load)
 
#load 2
load = Image.open("Dice Images\\dice2.jpg")
load = load.resize((200, 200))
two = ImageTk.PhotoImage(load)

#load 3
load = Image.open("Dice Images\\dice3.jpg")
load = load.resize((200, 200))
three = ImageTk.PhotoImage(load)

#load 4
load = Image.open("Dice Images\\dice4.jpg")
load = load.resize((200, 200))
four = ImageTk.PhotoImage(load)

#load 5
load = Image.open("Dice Images\\dice5.jpg")
load = load.resize((200, 200))
five = ImageTk.PhotoImage(load)

#load 6
load = Image.open("Dice Images\\dice6.jpg")
load = load.resize((200, 200))
six = ImageTk.PhotoImage(load)

load = Image.open("Dice Images\\black.jpg")
load = load.resize((200, 200))
black = ImageTk.PhotoImage(load)

#load = Image.open("C:\\Users\\HP\\Pictures\\heads.jpeg")
#load = load.resize((500, 400))
#black = ImageTk.PhotoImage(load)
def di():
    list1 = [1, 2, 3, 4, 5, 6]
    dice1 = random.choice(list1)
    #num = random.randint(0,1)
    if dice1 == 1:
        i.config(image=one)
    elif dice1 == 2:
        i.config(image=two)
    elif dice1 == 3:
        i.config(image=three)
    elif dice1 == 4:
        i.config(image=four)
    elif dice1 == 5:
        i.config(image=five)
    elif dice1 == 6:
        i.config(image=six)
    

b = Button(root, text="Roll", bg='lightblue', fg='white', activebackground="lightgray", padx=10, pady=10, command=di)
b.config(font=("Courier", 8))
b.pack()
 
i = Label(root, image=black)
i.pack()

e = Button(root, text="Exit", bg='gray', fg='white', activebackground="lightgray", padx=40, pady=20, command=exit)
e.config(font=("Courier", 14))
e.pack()

root.mainloop()