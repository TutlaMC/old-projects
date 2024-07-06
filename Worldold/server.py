from http import client
from ursinanetworking import *

server = UrsinaNetworkingServer('localhost',22625)
players=[]

app = Ursina()
import random
from perlin_noise import PerlinNoise
tests = 0
def runServerTest():
    global tests
    tests+=1
    print(f'Test#{tests}: Server has reponded with no current error')
terrain = Entity(model=None,collider=None)
noise = PerlinNoise(octaves=random.randint(10,1000000*10000),seed=random.randint(10,10000*10000))

world = []
@server.event
def onClientConnected(client):
    global players
    print('new player has joined!')
    
    players.append(client)
    runServerTest()
    #client.send_message('WDServer','chiekn')
    for i in players:
        runServerTest()
        
        i.send_message('AddPlayer',client)
    runServerTest()
    
        


@server.event
def SendPosition(Client,Content): 
    count = 0
    for i in players:
        
        
        i.send_message('ShowPlayerPos',[Client,Content])
        count+=1


def update():
    server.process_net_events()
app.run()