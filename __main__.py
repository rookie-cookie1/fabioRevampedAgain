from tkinter import * 
from PIL import Image,ImageTk
import tkinter as tk
#window setup code
win = tk.Tk()
loop = True
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()
img= ImageTk.PhotoImage(Image.open("fabio.png"))  
img= ImageTk.PhotoImage(Image.open("loogey.png"))       
        
        

win.mainloop()
