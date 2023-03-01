from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
import keyboard
import gameEngine
#window setup code
win = tk.Tk()
win.geometry("1817x860")
win.resizable(False, False)       
def mainMenuFunction(bName):
    if bName == 2:
        exit()
    elif bName == 1:
        pass
        print('Haha')
    elif bName == 0:
        win.destroy()

        
    else:
        print('ERROR: NO MATCHING BUTTON FUNCTION - PLEASE DEFINE IN "mainMenuFunction()"')
def MainMenu():
    #Calling this function brings up the visual main menu
    #The main menu layout is contained in this function
    global win
    global button
    #menuBackGround = Label(win, i = mainMenuImg)
    #menuBackGround.pack()
    YposSpace = 60
    adjustedY = 540
    xPos = 720
    exit =  tk.Button(
        win,
        text = 'Exit',
        width = 60,
        height = 3,
        bg = "brown",
        fg = "black",
        command=lambda: mainMenuFunction(2)
    ).place(x = 720, y = adjustedY)
    adjustedY = adjustedY - YposSpace
    options = tk.Button(
        win,
        text = 'Options',
        width = 60,
        height = 3,
        bg = "brown",
        fg = "black",
        command=lambda: mainMenuFunction(1)
    ).place(x = 720, y = adjustedY)
    adjustedY = adjustedY - YposSpace
    playGame = tk.Button(
        win,
        text = 'Play Game',
        width = 60,
        height = 3,
        bg = "brown",
        fg = "black",
        command=lambda: mainMenuFunction(0)
    ).place(x = 720, y = adjustedY)


#mainMenuImg = tk.PhotoImage(file = 'game_menu.png')
MainMenu()


win.mainloop()
gameEngine.gameFunc()