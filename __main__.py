from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
#window setup code
win = tk.Tk()
win.geometry("1817x860")
win.resizable(False, False)
def mainMenuFunction(bName):
    print(bName)
def MainMenu():
    #Calling this function brings up the visual main menu
    #The main menu layout is contained in this function
    global win
    global button
    menuBackGround = Label(win, i = mainMenuImg)
    menuBackGround.pack()
    YposSpace = 60
    adjustedY = 540
    playGame =  tk.Button(
        win,
        text = menuButtons[i],
        width = 60,
        height = 3,
        bg = "brown",
        fg = "black",
        command=lambda: mainMenuFunction(str())
    )


mainMenuImg = tk.PhotoImage(file = 'game_menu.png')
MainMenu()


win.mainloop()