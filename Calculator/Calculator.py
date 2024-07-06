from tkinter import *
import math

def button_press(num):

    global math_text

    

    math_text = math_text + str(num)

    math_label.set(math_text)

def equals():

    global math_text

    try:

        total = str(eval(math_text))

        math_label.set(total)

        math_text = total

    except SyntaxError:

        math_label.set("SYNTAX ERROR")

        math_text = ""

    except ZeroDivisionError:

        math_label.set("ZERO DIVISION ERROR")

        math_text = ""
    except Exception:
        math_label.set("MATH ERROR")

        math_text = ""


def clear():

    global math_text

    math_label.set("")

    math_text = ""



window = Tk()
window.title("TutCal")
window.geometry("500x500")

math_text = ""

math_label = StringVar()

label = Label(window, textvariable=math_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=0, column=3)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=0, column=4)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=0, column=5)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=1, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=1, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=1, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=1, column=3)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=1, column=4)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=5)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=0)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=2, column=1)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=2, column=2)

logb = Button(frame, text='log', height=4, width=9, font=70,
                 command=lambda: button_press('math.log('))
logb.grid(row=2, column=3)


sqrtb = Button(frame, text='sqrt', height=4, width=9, font=35,
                 command=lambda: button_press('math.sqrt('))
sqrtb.grid(row=2, column=4)

sinb = Button(frame, text='sin', height=4, width=9, font=35,
                 command=lambda: button_press('math.sin('))
sinb.grid(row=2, column=5)

rcurve = Button(frame, text='(', height=4, width=9, font=35,
                 command=lambda: button_press('('))
rcurve.grid(row=3, column=0)

lcurve = Button(frame, text=')', height=4, width=9, font=35,
                 command=lambda: button_press(')'))
lcurve.grid(row=3, column=1)

intb = Button(frame, text='Integer', height=4, width=9, font=35,
                 command=lambda: button_press('int('))
intb.grid(row=3, column=2)

exactb = Button(frame, text='Exact', height=4, width=9, font=35,
                 command=lambda: button_press('float('))
exactb.grid(row=3, column=3)

ceilb = Button(frame, text='EstUp', height=4, width=9, font=35,
                 command=lambda: button_press('math.ceil('))
ceilb.grid(row=3, column=4)

floorb = Button(frame, text='EstDown', height=4, width=9, font=35,
                 command=lambda: button_press('math.floor('))
floorb.grid(row=3, column=5)

clear = Button(frame, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.grid(row=5,column=0)

equal = Button(frame, text='=', height=4, width=12, font=70,
                 command=equals)
equal.grid(row=5, column=1)



window.mainloop()
