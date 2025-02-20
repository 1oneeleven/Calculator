
#the following code is the FC723 portflio assessment 3

import tkinter as tk
import math


class GUICalculator:
    def __init__(self,window):
        
        self.expression=""
        self.number_input=tk.StringVar()
        
        
        self.window=window
        self.window.title ("Calculator")  # set title
        self.window.geometry ("1000x800")  #set calculator window size
    
    
        self.entry = tk.Entry(self.window, textvariable=self.number_input, font=("Arial", 24), bd=20, relief="groove", justify="right", width=54)
        self.entry.grid(row=0, column=0, columnspan=4)
    
    
        self.buttons = [
            ['arcsin','arccos','arctan','√','C'],
            ['Sin','Cos','Tan','**2','='],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['(', ')', '0', '+']
        ]
        
        for i, row in enumerate(self.buttons):
            for j, button_text in enumerate(row):
                self.button = tk.Button(self.window, text=button_text, font=("Arial", 18), height=4, width=10, command=lambda button_text=button_text: self.on_click(button_text)) 
                                
                self.button.grid(row=i+1, column=j, padx=5, pady=5)
    
        
    
    def on_click(self, button_text):
        #add self.number_input to entry widget
        try:
            if button_text== '=':
                #evaluate the expression in number_input eval
                self.expression=eval(self.expression)
         
            #if statemetn to clear entry when "C" is pressed 
            elif button_text=='C':
                empty = ""
                self.expression.set(empty)
     
            elif button_text == 'sin':
                # use math.sin etc
                self.expression+='math.sin'
                
            elif button_text == 'cos':
                self.expression+=math.cos()
             
            elif button_text == 'tan':
                self.expression+=math.tan()
    
            elif button_text == 'arcsin': 
                self.expression+=math.arcsin()
                
            elif button_text == 'arccos':
                self.expression+=math.arccos()
                
            elif button_text == 'arctan':
                self.expression+=math.arctan()
           
            elif button_text == '√':
                self.expression+=math.sqrt()
            
            
            
            else:
                self.expression+=str(button_text)
                
            
        except:
            error = "error"
            self.expression.set(error)
            
        self.number_input.set(self.expression)
    
"""       
           
    def clear(self):
        empty = 0
        number_input.set(empty)
        
        return
        
       
    def addition(self): 
    
        
        return
        
    
    def subtraction(self):
        
        return
    
    def multiply(self):
        
        return
    
    def divide(self):
        
        return
    
    #_____________________________________
    
    def square(self): 
        
        return
    
    def sqrroot(self):
        
        return 
    
    #_____________________________________
    
    def sine(self):
        
        return
    
    def cosine(self):
        
        return
    
    def tangent(self):
        
        return
    
    #_____________________________________
    
    def arcsine(self):
        
        return
    
    def arccos(self):
        
        return
    
    def arctan(self):
        
        return
    

"""
window=tk.Tk()
calculator=GUICalculator(window)
window.mainloop()
