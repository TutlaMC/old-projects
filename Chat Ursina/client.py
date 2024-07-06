#from http import client
from logging import PlaceHolder
from ursinanetworking import *

from ursina import *
from tkinter import *
import tkinter

Client = UrsinaNetworkingClient('localhost',22625)

window = Tk() 



Frame = tkinter.Frame(window,height=10,width=10).pack()
box  = tkinter.Text(window,height=2,width=50)
abox  = tkinter.Text(window,height=1,width=20)
box.pack()
abox.pack()

def Send():
    global box
    text = box.get('1.0','end-1c')
    usrnam = abox.get('1.0','end-1c')
    text = usrnam+': '+text
    Client.send_message('SendMessage',text)
    print(text+'sending')
sb = Button(window,text='Send',command=Send).pack()

@Client.event
def ReciveMessage(Content):
    print('reciving message...')
    print(Content)
    Label = tkinter.Label(Frame,text=Content).pack()
    
while True:
    Client.process_net_events()

    window.update()

window.mainloop()




