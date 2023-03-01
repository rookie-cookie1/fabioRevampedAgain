import keyboard
from PIL import Image,ImageTk
import tkinter as tk
import keyboard

def gameFunc():
    win2 = tk.Tk()
    win2.geometry("1817x860")
    win2.resizable(False, False)
    theCanvas = tk.Canvas(
        win2, 
        bg = 'white', 
        height = 860, 
        width = 1817
        )
    coord = 10, 10, 300, 300
    arc = theCanvas.create_arc(coord, start=0, extent=150, fill="red")
    arv2 = theCanvas.create_arc(coord, start=150, extent=215, fill="green")
    theCanvas.pack()
    try:
        if keyboard.is_pressed("w"):
            print('im cumminggggg')
        if keyboard.is_pressed("a"):
            print('hehehe')
        if keyboard.is_pressed("s"):
            print('NO')
        if keyboard.is_pressed("d"):
            win2.destroy()
    except:
        win2.destroy()
    print('test')
    win2.mainloop()
