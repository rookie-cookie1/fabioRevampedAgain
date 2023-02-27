from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
#window setup code
win = tk.Tk()
win.geometry("1817x860")
win.resizable(False, False)

def MainMenu():
    #The main menu layout is contained in this function
    global win
    global button
    menuBackGround = Label(win, i = mainMenuImg)
    menuBackGround.pack()
    YposSpace = 60
    adjustedY = 540
    #Creates as menu buttons based off of the menuButtons list
    for item in menuButtons:
        button = tk.Button(
            win,
            text = item,
            width=60,
            height=3,
            bg="brown",
            fg="black",
        )
        button.pack()
        adjustedY =  adjustedY - YposSpace
        print(str(adjustedY))
        button.place(x = 720, y = adjustedY)

mainMenuImg = tk.PhotoImage(file = 'game_menu.png')
menuButtons = ['Exit Game', 'Options', 'Play Game']
MainMenu()


win.mainloop()