from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
#window setup code
win = tk.Tk()

canvas = Canvas(win, width = 1500, height = 900)
canvas.pack()
img2 = Image.open("loogey.png")
img2 = img2.resize((1500, 900)) 
img2 = ImageTk.PhotoImage(img2)
canvas.create_image(10,10,anchor=NW,image=img2)

button = tk.Button(
    text="Play",
    width=50,
    height=10,
    bg="brown",
    fg="black",
)
button.pack()
win.mainloop()