import tkinter

window = tkinter.Tk()

def ds(event):
    print(event.keysym)

window.bind("<Control_L>s",ds)

window.mainloop()