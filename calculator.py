from tkinter import *
cal=Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
txtDisplay=Entry(cal,font=('Arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

bt7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7),bg="powder blue").grid(row=1,column=0)
bt8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8),bg="powder blue").grid(row=1,column=1)
bt9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9),bg="powder blue").grid(row=1,column=2)
addition=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+"),bg="powder blue").grid(row=1,column=3)

bt4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4),bg="powder blue").grid(row=2,column=0)
bt5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5),bg="powder blue").grid(row=2,column=1)
bt6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6),bg="powder blue").grid(row=2,column=2)
subtraction=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-"),bg="powder blue").grid(row=2,column=3)

bt1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1),bg="powder blue").grid(row=3,column=0)
bt2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2),bg="powder blue").grid(row=3,column=1)
bt3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3),bg="powder blue").grid(row=3,column=2)
multi=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*"),bg="powder blue").grid(row=3,column=3)

bt0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0),bg="powder blue").grid(row=4,column=0)
btclear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=lambda:btnclear(),bg="powder blue").grid(row=4,column=1)
btequals=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=lambda:btnequal(),bg="powder blue").grid(row=4,column=2)
division=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/"),bg="powder blue").grid(row=4,column=3)

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnclear():
    global operator
    operator=""
    text_input.set("")
def btnequal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
cal.mainloop()