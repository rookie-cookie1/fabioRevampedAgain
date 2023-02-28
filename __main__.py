from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
import keyboard
#window setup code
win = tk.Tk()
win.geometry("1817x860")
win.resizable(False, False)
def gameFunc():
    theCanvas = tk.Canvas(
        win, 
        bg = 'white', 
        height = 860, 
        width = 1817
        )
    coord = 10, 10, 300, 300
    arc = theCanvas.create_arc(coord, start=0, extent=150, fill="red")
    arv2 = theCanvas.create_arc(coord, start=150, extent=215, fill="green")
    theCanvas.pack()
    while True:
        try:
            if keyboard.is_pressed("w"):
                print('im cumminggggg')
            if keyboard.is_pressed("a"):
                print('hehehe')
            if keyboard.is_pressed("s"):
                print('NO')
            if keyboard.is_pressed("d"):
                break
        except:
            break
        
def mainMenuFunction(bName):
    if bName == 2:
        exit()
    elif bName == 1:
        pass
        print('Haha')
    elif bName == 0:
        gameFunc()
        print('Bruh')
    else:
        print('ERROR: NO MATCHING BUTTON FUNCTION - PLEASE DEFINE IN "mainMenuFunction()"')
def MainMenu():
    #Calling this function brings up the visual main menu
    #The main menu layout is contained in this function
    global win
    global button
    menuBackGround = Label(win, i = mainMenuImg)
    menuBackGround.pack()
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


mainMenuImg = tk.PhotoImage(file = 'game_menu.png')
MainMenu()


win.mainloop()