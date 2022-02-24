from tkinter import *
cal=Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
txtDisplay=Entry(cal,font=('Arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)
