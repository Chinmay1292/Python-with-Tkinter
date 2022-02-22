import tkinter 
import random 
colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30 
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour() 
def nextColour():
    global score 
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))