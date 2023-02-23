from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk


menuButtons = ['Play Game', 'Settings', 'Options']
for index in len(menuButtons):
    tk.Button(
        text = menuButtons[index]
        width = 60
        height = 3
        
    ).pack

#window setup code
win = tk.Tk()
win.geometry("1817x900")
win.resizable(False, False)
mainMenuImg = tk.PhotoImage(file = 'game_menu.png')
menuBackGround = Label(win, i = mainMenuImg)
button = tk.Button(
    text="Play",
    width=60,
    height=3,
    bg="brown",
    fg="black",
)
menuBackGround.pack()

button.pack()
button.place(x = 720, y = 500)
win.mainloop()