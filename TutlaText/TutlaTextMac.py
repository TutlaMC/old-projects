import os
import sys
import pyperclip
import webbrowser
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import time
import subprocess
import win32api
import win32print

file_path = ''





def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def set_file_path(path):
    global file_path
    file_path = path
    window.title(file_path)

def open_file():
    path = askopenfilename(filetypes=[('All Files','*.*'),('Html Files','*.html'),('Cascading Style Sheets (CSS) Files','*.css'),('Javascript','*.js'),('Python Files', '*.py')])
    try:
        with open(path, 'r') as file:
            code = file.read()
            text_area.delete('1.0', END)
            text_area.insert('1.0', code)
            set_file_path(path)
    except Exception:
         showerror('Aborted', 'File not supported or open window closed')


def save_file():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('All Files','*.*'),('Html Files','*.html'),('Cascading Style Sheets (CSS) Files','*.css'),('Javascript','*.js'),('Python Files', '*.py')])
    else:
        path = file_path


    try:
        with open(path, 'w') as file:
            code = text_area.get('1.0', END)
            file.write(code)
            set_file_path(path)
    except Exception:
        showinfo("Closed", "Closed or falied to save")

def saveAs_file():
    path = asksaveasfilename(filetypes=[('All Files','*.*'),('Html Files','*.html'),('Cascading Style Sheets (CSS) Files','*.css'),('Javascript','*.js'),('Python Files', '*.py')])
    path = file_path


    try:
        with open(path, 'w') as file:
            code = text_area.get('1.0', END)
            file.write(code)
            set_file_path(path)
    except Exception:
        showinfo("Closed", "Closed or falied to save")


def cut(event):
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About","This program is made by Tutla. \n you can create any file realated to TEXT. \n This is completly OPEN SOURCE")

def sourceCode():
    showinfo("Source Code","Source code provided in install link.")


def bold_text():
    boldFont = font.Font(text_area, text_area.cget("font"))
    boldFont.configure(weight="bold")

    text_area.tag_configure("bold",font=boldFont)
    
    try:
        current_tags = text_area.tag_names("sel.first")
        if "bold" in current_tags:
            text_area.tag_remove("bold", "sel.first","sel.last")
        else:
            text_area.tag_add("bold", "sel.first","sel.last")
    except Exception:
        return



def italic_text():
    italicFont = font.Font(text_area, text_area.cget("font"))
    italicFont.configure(slant="italic")


    text_area.tag_configure("italic",font=italicFont)
    
    try:
        current_tags = text_area.tag_names("sel.first")
        if "italic" in current_tags:
            text_area.tag_remove("italic", "sel.first","sel.last")
        else:
            text_area.tag_add("italic", "sel.first","sel.last")
    except Exception:
        return


def selectAT():
    text_area.tag_add('sel','1.0','end')


def clearAT():
    text_area.delete(1.0,END)

def rpython():   

    if file_path == '':
       showwarning("Code Not Found","Please save your file!")
       return
    else:
        rpythonw = Tk()
        rpythonw.title("Python Output Window (POW)")
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        rlabel = Text(rpythonw, height=10)
        rlabel.pack()
        rlabel.insert('1.0', output)
        rlabel.insert('1.0',  error)


        rpythonw.mainloop()

def rhtml():
     if file_path == '':
       showwarning("Code Not Found","Please save your file!")
       return
     else:
        webbrowser.open(file_path)
        
def print_file():
    printer_name = win32print.GetDefaultPrinter()
    to_print = file_path

    if to_print:
        try:
            win32api.ShellExecute(0, 'print', to_print, None, ".",0)
        except Exception:
            showwarning("Printer Not Found","Printer Not Found or \n Your printer has not been Turned on!")
    else:
        to_print = askopenfilename(filetypes=[('All Files','*.*'),('PDF files','*.pdf'),('Html Files','*.html'),('Cascading Style Sheets (CSS) Files','*.css'),('Javascript','*.js'),('Python Files', '*.py')])
        try:
            win32api.ShellExecute(0, 'print', to_print, None, ".",0)
        except Exception:
            showwarning("File Not Found","You have canceled print!")



def quit():
    window.destroy()


window = Tk()
window.title("TutlaText")
iconM = PhotoImage(file="C:\\Users\\ayaan\\Desktop\\Tutla\\PythonProjects\\TutlaText\\t.png")
window.iconphoto(True,iconM)

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# come back here!
font_name = StringVar(window)
font_name.set("Arial")

cfcolor = 'black'

font_size = StringVar(window)
font_size.set("25")

def fontss():
    fontsw = Tk()
    
    def change_font(*args):
        text_area.config(font=(font_name.get(), size_box.get()))

    


    fontsw.mainloop()

def change_color():
    global cfcolor
    fcolor = colorchooser.askcolor(title="Font Color")
    cfcolor = fcolor
    text_area.config(fg=fcolor[1])

def overstrike(*args):
    try:

        current_tags = text_area.tag_names("sel.first")
        if "overstrike" in current_tags:
            text_area.tag_remove("overstrike", "sel.first", "sel.last")
        else:
            text_area.tag_add("overstrike", "sel.first", "sel.last")
            overstrike_font = font.Font(text_area, text_area.cget("font"))
            overstrike_font.configure(overstrike=1)
            text_area.tag_configure("overstrike", font=overstrike_font)
    except Exception:
        return


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))
    

def adimg():
    gcft = askopenfilename(filetypes=[('PNG','*.png')])
    cft = PhotoImage("C:\\Users\\ayaan\\Desktop\\Tutla\\TutlaWebsite\\Images\\MainImg3.png")
    icposition = text_area.index(INSERT)
    text_area.image_create(END, image=cft)



notepad = ttk.Notebook(window)
hometab = Frame(notepad, height=100, width=100)
notepad.add(hometab, text="Home")

font_box = OptionMenu(hometab, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(hometab, from_=1, to=1000, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

fontcolor = Button(hometab, text = "Change Font Color", command=change_color).grid(row=0, column=5)
addimgb = Button(hometab, text="Add image!",command=adimg).grid(row=0,column=7)

pasteb = Button(hometab,text="Paste",font=(17),command=paste).grid(row=1,column=0)
copyb = Button(hometab,text="Copy",font=(17),command=copy).grid(row=1,column=1)
cutb = Button(hometab, text="Cut ",font=(17),command=cut).grid(row=1,column=2)


cutb = Button(hometab, text="STRIKE!",font=(17),command=overstrike).grid(row=1,column=3)

bb = Button(hometab, text="B", font=('Bahnschrift SemiBold SemiConden',17), command=bold_text).grid(row=1,column=5)
ib = Button(hometab, text="I", font=('Ink free',16), command=italic_text).grid(row=1,column=4)

notepad.pack()

frame = Frame(window)
frame.pack()

text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)
text_scrollH = Scrollbar(frame, orient="horizontal")
text_scrollH.pack(side=BOTTOM, fill=X)

text_area = Text(frame, font=(font_name.get(), font_size.get()),wrap="none", width=80, height=15, yscrollcommand=text_scroll.set, xscrollcommand=text_scrollH.set)
text_area.pack(side=BOTTOM)

text_scroll.config(command=text_area.yview)
text_scrollH.config(command=text_area.xview)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file,accelerator="(Cmd+S)")
file_menu.add_command(label="Save As", command=saveAs_file,accelerator="(Cmd+Shift+S)")
file_menu.add_separator()
file_menu.add_command(label="Print (Not supported in MacOS)", command=print_file,accelerator="(Cmd+Shift+P)")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit,accelerator="(Alt+F4)")

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut,accelerator="(Cmd+X)")
edit_menu.add_command(label="Copy", command=copy,accelerator="(Cmd+C)")
edit_menu.add_command(label="Paste", command=paste,accelerator="(Cmd+V)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text_area.edit_undo,accelerator="(Cmd+Z)")
edit_menu.add_command(label="Redo", command=text_area.edit_redo,accelerator="(Cmd+yY")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=selectAT,accelerator="(Cmd+Z)")
edit_menu.add_command(label="Clear",command=clearAT,accelerator="(Cmd+A+Backspace)")


Code_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Code", menu=Code_menu)
run_code_menu = Menu(Code_menu, tearoff=0)
Code_menu.add_cascade(label="Run", menu=run_code_menu)
run_code_menu.add_command(label="Python",command=rpython)
run_code_menu.add_command(label="HTML",command=rhtml)


help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Source Code", command=sourceCode)

window.bind("<Control_L>s",save_file)

window.mainloop()
