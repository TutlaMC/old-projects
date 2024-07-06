from http import client
from ursinanetworking import *

server = UrsinaNetworkingServer('localhost',22625)
#players=[]

app = Ursina()
#import random
#from perlin_noise import PerlinNoise
tests = 0
def runServerTest():
    global tests
    tests+=1
    print(f'Test#{tests}: Server has reponded with no current error')

@server.event
def onClientConnected(client):
    #global players
    print('New person in the chat!')
    runServerTest()
    #players.append(client)


@server.event
def SendMessage(client,Content): 
    print(Content)
    server.broadcast('ReciveMessage',Content)
    print('Sent')
    


def update():
    server.process_net_events()
app.run()