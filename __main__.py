from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
#window setup code
win = tk.Tk()
mainMenuImg = tk.PhotoImage(file = 'game_menu.png')
menuBackGround = Label(win, i = mainMenuImg)
button = tk.Button(
    text="Play",
    width=60,
    height=3,
    bg="brown",
    fg="black",
)
button.pack()
menuBackGround.pack()
win.mainloop()