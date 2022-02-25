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

def RealTimeCurrencyConversion(): 
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()
    
    from_currency = variable1.get() 
    to_currency = variable2.get()
    
    if (Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Error !!","Amount Not Entered.\n Please a valid amount.")
        
    elif (from_currency=="currency" or to_currency=="currency"):
        tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")
        
    else:
        new_amt = c.convert(from_currency,to_currency,float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount)) 


def clear_all() : 
	Amount1_field.delete(0, tk.END) 
	Amount2_field.delete(0, tk.END)
    
    
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]


root.configure(background = '#e6e5e5') 
root.geometry("700x400") 

Label_1 =Label(root, font=('lato black', 27,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=1, column=0,sticky=W)


label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    Amount  :  ", bg="#e6e5e5",fg = "black") 
label1.grid(row=2, column=0,sticky=W)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    From Currency  :  ", bg="#e6e5e5",fg = "black") 
label1.grid(row=3, column=0,sticky=W)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    To Currency  :  ", bg="#e6e5e5",fg = "black") 
label1.grid(row=4, column=0,sticky=W)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    Converted Amount  :  ", bg="#e6e5e5",fg = "black") 
label1.grid(row=8, column=0,sticky=W)


Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=5, column=0,sticky=W)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=7, column=0,sticky=W)


