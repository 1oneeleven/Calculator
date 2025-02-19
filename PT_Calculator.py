
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

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(window, text=button_text, font=("Arial", 18), height=4, width=10,
                           command=lambda button_text=button_text: on_click(button_text))
        button.grid(row=i+1, column=j, padx=5, pady=5)
number_input = 0


def close_window():
    
    window.destroy()

def delete():
   global empty
   empty = 0
   number_input.set(empty)
   
def clear():
    
    
   
def addition(): 

    
    return
    

def subtraction():
    
    return

def multiply():
    
    return

def divide():
    
    return

#_____________________________________

def square(): 
    
    return

def sqrroot():
    
    return 

#_____________________________________

def sine():
    
    return

def cosine():
    
    return

def tangent():
    
    return

#_____________________________________

def arcsine():
    
    return

def arccos():
    
    return

def arctan():
    
    return



window.mainloop()