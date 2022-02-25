import tkinter as tk
from tkinter import *
import tkinter.messagebox
 
root = tk.Tk() 

root.title("GUI : Currency Conversion")
root.geometry("600x400")

Tops = Frame(root,pady = 2, width =3000, height = 100, relief = "ridge")
Tops.grid(row=0,column=0)


headlabel = tk.Label(Tops,font=('lato black', 19,'bold'), text = '      TechnoLord Programming : Currency Converter     ') 
headlabel.pack(padx=10, pady=0)
 
variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 
 
variable1.set("currency") 
variable2.set("currency") 