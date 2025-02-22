
#the following code is the FC723 portflio assessment 3

import tkinter as tk
#Import math module
import math 
#Import trigonometric and special function from the math module
from math import sin, cos, tan, asin, acos, atan, sqrt


'''Create class for the calculator GUI'''
class GUICalculator:
    def __init__(self,window):
        
        #Initialize expression for calculator
        self.expression=""
        self.number_input=tk.StringVar()
    
        #Create main window
        self.window=window
        self.window.title ("Calculator")  #set title for window
        self.window.geometry ("800x1000")  #set calculator window size
    
        # Create an input box to display the calculation result or input content
        self.entry = tk.Entry(self.window, textvariable=self.number_input, font=("Arial", 24), bd=20, relief="groove", justify="right", width=54)
        #set position for the input box into the window's grid
        self.entry.grid(row=0, column=0, columnspan=4)
    
        #Define the matrix button layout of calculator buttons in a 2D list 
        self.buttons = [
            ['arcsin','arccos','arctan','√'],
            ['Sin','Cos','Tan','**2'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'Clear', '+'],
            ['(',')','=']
        ]
        
        #Create and place buttons in calculator window in a grid pattern
        for i, row in enumerate(self.buttons):
            # Create buttons and bind click events to each button
            for j, button_text in enumerate(row):
                self.button = tk.Button(self.window, text=button_text, font=("Arial", 18), height=4, width=10, command=lambda button_text=button_text: self.on_click(button_text)) 
                #Set grid posttions for buttons
                self.button.grid(row=i+1, column=j, padx=5, pady=4)
                
        
    
    def on_click(self, button_text):
        
        
        ''' Try function to handle click events '''
        
        
        try:
            if button_text== '=':
                #Evaluate the mathematical expression in number_input
                self.expression=eval(self.expression)
         
            #Clear expression is "=" button is pressed
            elif button_text=='Clear':
                self.expression = ""
                
            #Calulate Trigonometric and special functions imported from math module
            #Calculates Sin
            elif button_text == 'Sin':
                self.expression+='sin'
            
            #Calculates Cosine
            elif button_text == 'Cos':
                self.expression+= 'cos'
             
            #Calculates Tangent
            elif button_text == 'Tan':
                self.expression+= 'tan'
    
            #Calculates Arcsin
            elif button_text == 'arcsin': 
                self.expression+= 'asin'
                
            #Calculates Arccos
            elif button_text == 'arccos':
                self.expression+= 'acos'
                
            #Calculates Arctan
            elif button_text == 'arctan':
                self.expression+= 'atan'
                
           #Calculates Squareroot 
            elif button_text == '√':
                self.expression+= 'sqrt'
            
            
            else:
                #Keep adding the button inputs to a string in button_text
                self.expression+=str(button_text)
                
            
        except:
            #Handle evaluation errors, could be depending on different math principles
            self.expression = "error"
            
        #Update the entry widget to the expression following the try function
        self.number_input.set(self.expression)
    

#Create and execute the Calculator window
window=tk.Tk()
calculator=GUICalculator(window)
window.mainloop()
