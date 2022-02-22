import tkinter 
import random 
colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30 
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour() 