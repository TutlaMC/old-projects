#from http import client
from logging import PlaceHolder
from ursinanetworking import *
import random
from ursina import *


Client = UrsinaNetworkingClient('localhost',22625)

window = Ursina()
playerpos=None
playerNumber = None
players = []
playerPositions = []
player=Entity(model='cube',position=(random.randint(0,10),random.randint(0,10),random.randint(0,5)))


@Client.event
def SendPosition():
    
    Client.send_message('SendPosition',[playerNumber,player.position])

@Client.event
def AddPlayer(Content):
    global playerNumber
    if playerNumber==None: playerNumber=Content
    else:
        players.append([Content,Entity(model='cube', position=(random.randint(0,10),random.randint(0,10),random.randint(0,5)))])
@Client.event
def RecivePosition(Content):
    Tplayer = players.index(Content[0])
    Theplayer= Tplayer[1]
    Theplayer.postion = Content[1]

def input():
    playerpos = player.position
    Client.process_net_events()
    Client.send_message('SendPosition',playerpos)
window.run()







