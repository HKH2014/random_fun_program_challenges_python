import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("1000x500")

bgimg = tk.PhotoImage(file="bgIMG.jpg")
bglabel = Label(window, image=bgimg)
bglabel.place(relwidth=1, relheight=1)

window.mainloop()
