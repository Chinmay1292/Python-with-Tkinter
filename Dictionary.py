from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()

root.geometry("400x400")
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

Label(root, text="Dictionary", font=("Arial 22 italic"), fg="Red").pack(pady=10)

frame = Frame(root)

Label(frame, text="Type Word", font=("Arial 16 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning: ", font=("Arial 12 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Arial 12"))
meaning.pack()
frame1.pack(pady=10)

frame2 = Frame(root)
Label(frame2, text="Synonym: ", font=("Arial 12 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Arial 12"))
synonym.pack()
frame.pack(pady=10)

frame3 = Frame(root)
Label(frame3, text="Antonym: ", font=("Arial 12 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Arial 12"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root, text="Submit", font=("Helvetica 16 bold"), command=dict).pack()

root.mainloop()