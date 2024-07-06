#from http import client
from logging import PlaceHolder
from ursinanetworking import *
import speech_recognition as sr
import pyttsx3
from ursina import *
from tkinter import *
import tkinter

Client = UrsinaNetworkingClient('localhost',22625)

window = Tk() 

talker = pyttsx3.init()

def talk(text):
    print(text)
    talker.say(text)
    talker.runAndWait()
listener = sr.Recognizer()
Frame = tkinter.Frame(window,height=10,width=10).pack()

abox  = tkinter.Text(window,height=1,width=20)

abox.pack()

def Send():
    talk('listening')
    with sr.Microphone() as source:
     
        voice = listener.listen(source)
        text = listener.recognize_google(voice)
        text = text.lower()
        print(text)
    usrnam = abox.get('1.0','end-1c')
    text = usrnam+' says '+text
    Client.send_message('SendMessage',text)
    print(text+'sending')
sb = Button(window,text='Mic',command=Send).pack()

@Client.event
def ReciveMessage(Content):
    print('reciving message...')
    print(Content)
    talk(Content)
    
    
while True:
    Client.process_net_events()

    window.update()

window.mainloop()




