
#the following code is the FC723 portflio assessment 3

import tkinter as tk
import math
from math import sin, cos, tan, asin, acos, atan, sqrt


class GUICalculator:
    def __init__(self,window):
        
        self.expression=""
        self.number_input=tk.StringVar()
        
        
        self.window=window
        self.window.title ("Calculator")  # set title
        self.window.geometry ("800x1000")  #set calculator window size
    
    
        self.entry = tk.Entry(self.window, textvariable=self.number_input, font=("Arial", 24), bd=20, relief="groove", justify="right", width=54)
        self.entry.grid(row=0, column=0, columnspan=4)
    
    
        self.buttons = [
            ['arcsin','arccos','arctan','√'],
            ['Sin','Cos','Tan','**2'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['(', ')', '0', '+'],
            ['C','=','.']
        ]
        
        for i, row in enumerate(self.buttons):
            for j, button_text in enumerate(row):
                self.button = tk.Button(self.window, text=button_text, font=("Arial", 18), height=4, width=10, command=lambda button_text=button_text: self.on_click(button_text)) 
                                #The size of the window and the textbox the font
                self.button.grid(row=i+1, column=j, padx=5, pady=4)
                # Create buttons and add them to the grid
        
    
    def on_click(self, button_text):
        #add self.number_input to entry widget
        try:
            if button_text== '=':
                #evaluate the expression in number_input eval
                self.expression=eval(self.expression)
         
            #if statemetn to clear entry when "C" is pressed    
            elif button_text=='C':
                self.expression = ""
     
            elif button_text == 'Sin':
                
                
                self.expression+='sin'
                
            elif button_text == 'Cos':
                self.expression+= 'cos'
             
            elif button_text == 'Tan':
                self.expression+= 'tan'
    
            elif button_text == 'arcsin': 
                self.expression+= 'asin'
                
                
            elif button_text == 'arccos':
                self.expression+= 'acos'
                
                
            elif button_text == 'arctan':
                self.expression+= 'tan'
                
           
            elif button_text == '√':
                self.expression+= 'sqrt'
            
            
            else:
                self.expression+=str(button_text)
                
            
        except:
            
            self.expression = "error"
            
        self.number_input.set(self.expression)
    

window=tk.Tk()
calculator=GUICalculator(window)
window.mainloop()
