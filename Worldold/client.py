from http import client
from ursinanetworking import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.prefabs.health_bar import HealthBar
import random
from perlin_noise import PerlinNoise

client = UrsinaNetworkingClient('localhost',22625)
app=Ursina()
noise =  ''
players = []


player = Entity(model='cube', position=(random.randint(1,15),10,random.randint(1,15) ))
def getPlayerPosition():
    return player.position
@client.event
def onConnectionEstablished(client):
    print('lets goo!')
@client.event
def onConnectionError(error):
    print('player has left')
@client.event
def SendPosition(Content): 
    print('yea')
@client.event
def WDServer(Content):
    client.send_message('SendPosition',str(getPlayerPosition()))
@client.event
def ShowPlayerPos(Content):
    pass
@client.event 
def AddPlayer(player):
    global players
    players.append([player,Entity(model='cube',position=(random.randint(1,15),10,random.randint(1,15)))])

    
    

    

def update():
    client.process_net_events()
app.run()