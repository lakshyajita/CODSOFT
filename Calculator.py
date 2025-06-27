from tkinter import *

def press_button(num):
    global expression
    expression = expression + str(num)
    eqn_text.set(expression)

def equalsto():
    global expression
    try:
        result = str(eval(expression))
        eqn_text.set(result)
        expression = result
    except:
        eqn_text.set("ERROR")

def clear():
    global expression
    eqn_text.set("")
    expression = ""

def backspace():
    current = eqn_text.get()
    eqn_text.set(current[:-1])

window = Tk()

window.title("Calculator")
window.geometry("400x500")

expression = ""
eqn_text = StringVar()

frame = Frame(window, relief = RIDGE, bd = 3)
frame.pack()

label = Label(frame, textvariable = eqn_text ,font = ('Monospace', 20),
              width = 15, height = 2,
              relief = SUNKEN,
              bg ='white', fg = 'black')
label.grid(row = 0, column = 0, columnspan = 4)

button7 = Button(frame, text = 7, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(7))
button7.grid(row = 1, column = 0)

button8 = Button(frame, text = 8, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(8))
button8.grid(row = 1, column = 1)

button9 = Button(frame, text = 9, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(9))
button9.grid(row = 1, column = 2)

button4 = Button(frame, text = 4, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(4))
button4.grid(row = 2, column = 0)

button5 = Button(frame, text = 5, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(5))
button5.grid(row = 2, column = 1)

button6 = Button(frame, text = 6, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(6))
button6.grid(row = 2, column = 2)

button3 = Button(frame, text = 3, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(3))
button3.grid(row = 3, column = 0)

button2 = Button(frame, text = 2, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(2))
button2.grid(row = 3, column = 1)

button1 = Button(frame, text = 1, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(1,))
button1.grid(row = 3, column = 2)

button0 = Button(frame, text = 0, height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button(0))
button0.grid(row = 4, column = 0)

decimal = Button(frame, text = '.', height = 4, width = 7, relief = RAISED,
                 command = lambda:press_button('.'))
decimal.grid(row = 4, column = 1)

devide = Button(frame, text = '/', height = 4, width = 7, relief = RAISED,
                command = lambda:press_button('/'))
devide.grid(row = 1, column = 3)

multiply = Button(frame, text = '*', height = 4, width = 7, relief = RAISED,
                  command = lambda:press_button('*'))
multiply.grid(row = 2, column = 3)

minus = Button(frame, text = '-', height = 4, width = 7, relief = RAISED,
               command = lambda:press_button('-'))
minus.grid(row = 3, column = 3)

plus = Button(frame, text = '+', height = 4, width = 7, relief = RAISED,
              command = lambda:press_button('+'))
plus.grid(row = 4, column = 3)

backspace_btn = Button(frame, text = 'C', height = 4, width = 7, relief = RAISED,
                   command = backspace)
backspace_btn.grid(row = 4, column = 2)

allclear = Button(frame, text = 'AC', height = 3, width = 16, relief = RAISED,
               command = clear)
allclear.grid(row = 5, column = 0, columnspan = 2)

equals = Button(frame, text = '=', height = 3, width = 16, relief = RAISED,
                command = equalsto)
equals.grid(row = 5, column = 2, columnspan = 2)

window.mainloop()