
#the following code is the FC723 portflio assessment 3

import tkinter as tk
import math


window = tk.Tk ()  #TK () method to initialise a main window
window.title ("Calculator")  # set title
window.geometry ("800x600")  #set calculator window size

entry = tk.Entry(window, font=("Arial", 24), bd=20, relief="groove", justify="right", width=54)
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ['','','','√',]
    ['Sin','Cos','Tan','^'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]
window.mainloop()