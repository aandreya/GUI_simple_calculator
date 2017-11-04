from Tkinter import *
import Tkinter
import math
import random
import tkMessageBox

def math_op():
    number_one = float(firstNumber_entry.get())
    operator = variable.get()
    number_two = float(secondNumber_entry.get())

    if operator == "+":
        plus = number_one + number_two
        output = plus
    elif operator == "-":
        minus = number_one - number_two
        output = minus
    elif operator == "*":
        krat = number_one * number_two
        output = krat
    elif operator == "/":
        deljeno = number_one / number_two
        output = deljeno
    math_result_label.config(text=output)

def reset():
    firstNumber_entry.delete(0, Tkinter.END)
    secondNumber_entry.delete(0, Tkinter.END)
    math_result_label.config(text="")

window = Tkinter.Tk()
window.geometry("300x400")
window.title("Calculator")
greeting = Tkinter.Label(window, text = "Let's do some M A T H\n\n")
greeting.pack()

firstNumber = Tkinter.Label(window, text = ("Enter first number: "))
firstNumber.pack()
firstNumber_entry = Tkinter.Entry()   #vnosno okno
firstNumber_entry.pack()

toOperation = Tkinter.Label(window, text = ("\nChoose the mathematical operation:"))
toOperation.pack()
variable = StringVar(window)        #dropdown meni
variable.set("+")                   #primarno videno v dropdown
chooseOperation = OptionMenu(window, variable, "+", "-", "*", "/")
chooseOperation.pack()

secondNumber = Tkinter.Label(window, text = ("\nEnter second number: "))
secondNumber.pack()
secondNumber_entry = Tkinter.Entry()   #vnosno okno
secondNumber_entry.pack()

placeHolder = Tkinter.Label(window, text = ("\n"))
placeHolder.pack()
submit_button_pushed = Tkinter.Button(window, text="Submit", command = math_op)
submit_button_pushed.pack()
reset_button_pushed = Tkinter.Button(window, text="Reset", command = reset)
reset_button_pushed.pack()
result = Tkinter.Label(window, text = ("\nResult is:"))
result.pack()
math_result_label = Tkinter.Label(window, text="")
math_result_label.pack()

window.mainloop()

