from http import client
from ursinanetworking import *

server = UrsinaNetworkingServer('localhost',22625)
#players=[]

app = Ursina()
#import random
playerNumber = 0
#from perlin_noise import PerlinNoise
tests = 0
def runServerTest():
    global tests
    tests+=1
    print(f'Test#{tests}: Server has reponded with no current error')

@server.event
def onClientConnected(client):
    #global players
    global playerNumber
    print('New person in the game!')
    runServerTest()
    playerNumber+=1
    server.broadcast('AddPlayer',playerNumber)
    #players.append(client)


@server.event
def SendPosition(client,Content): 
    print(Content)
    server.broadcast('RecivePosition',Content)
    
    


def update():
    server.process_net_events()
app.run()