import pywhatkit
from tkinter import *

window = Tk()

text = Text(window)
text.pack()

def work():
    handwriting=text.get("1.0", "end-1c")
    pywhatkit.text_to_handwriting(handwriting)

button = Button(window, text="Convert",command=work).pack()



window.mainloop()
