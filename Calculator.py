from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.iconbitmap('D:\SAYAN\Python Course\TKinter Files\calc.ico')
#Creating InputBox

box = Entry(root, width = 45, borderwidth=5)
box.grid(row =0,column=0, columnspan=3, padx = 0, pady = 0)

def button_func(number):                        # To Display Number in InputBox
    current = box.get()
    box.delete(0,END)
    box.insert(0,str(current)+ str(number))     
def button_clear():                            # AC Button Function
    box.delete(0,END)
def button_string(sign):                      # To Display the Sign
    box.insert(len(box.get()),sign)
def calc():                                  # Performing the calculations
    word = box.get()
    if(word.find("+")!= -1):
        result = float(word[0:word.index("+")]) + float(word[(word.index("+")+1):])
        if result%1 == 0:
            result = int(result)
    elif(word.find("-") != -1):
        result = float(word[0:word.index("-")]) - float(word[(word.index("-")+1):])
        if result%1 == 0:
            result = int(result)
    elif(word.find("/") != -1):
        result = float(word[0:word.index("/")]) / float(word[(word.index("/")+1):])
        if result%1 == 0:
            result = int(result)
    elif(word.find("*") != -1):
        result = float(word[0:word.index("*")]) * float(word[(word.index("*")+1):])
        if result%1 == 0:
            result = int(result)
    box.delete(0,END)
    box.insert(0, result)        
    
#Creating NumberPad
button1 = Button(root, text = "1", padx= 40, pady= 20, command = lambda: button_func(1))
button2 = Button(root, text = "2", padx= 40, pady= 20, command = lambda: button_func(2))
button3 = Button(root, text = "3", padx= 40, pady= 20, command = lambda: button_func(3))
button4 = Button(root, text = "4", padx= 40, pady= 20, command = lambda: button_func(4))
button5 = Button(root, text = "5", padx= 40, pady= 20, command = lambda: button_func(5))
button6 = Button(root, text = "6", padx= 40, pady= 20, command = lambda: button_func(6))
button7 = Button(root, text = "7", padx= 40, pady= 20, command = lambda: button_func(7))
button8 = Button(root, text = "8", padx= 40, pady= 20, command = lambda: button_func(8))
button9 = Button(root, text = "9", padx= 40, pady= 20, command = lambda: button_func(9))
button0 = Button(root, text = "0", padx= 40, pady= 20, command = lambda: button_func(0))

#Creating CalculatorFunctions

button_add = Button(root, text = "+", padx= 40, pady= 20, command = lambda: button_string("+"))
button_AC = Button(root, text = "AC", padx= 35, pady= 20, command = lambda: button_clear())
button_equals = Button(root, text= "=", padx = 100 , pady = 20, command = lambda: calc())
button_subtract = Button(root, text = "-", padx= 40, pady= 20, command = lambda: button_string("-"))
button_mul = Button(root, text = "*", padx= 40, pady= 20, command = lambda: button_string("*"))
button_div = Button(root, text = "/", padx= 40, pady= 20, command = lambda: button_string("/"))


#Aligning Buttons

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button0.grid(row = 4, column = 0)
button_add.grid(row = 4, column = 1)
button_subtract.grid(row = 4, column = 2)
button_mul.grid(row = 5, column = 0)
button_div.grid(row = 5, column = 1)
button_AC.grid(row = 5, column = 2)
button_equals.grid(row =6, column = 0, columnspan = 3)





root.mainloop()