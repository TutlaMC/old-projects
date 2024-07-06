from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.prefabs.health_bar import HealthBar
import random

app = Ursina()
seed = 35
world = []
def get_WorldData():
    print('----worldata----')
    print(world)
def yn():
    a = random.randint(1,seed)
    return a
class Block(Button):
    def __init__(self,sizeY=(1,1,1), position=(0,0,0),hcolor=color.lime, scolor=color.green):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            size = sizeY,
            texture = 'grass',
            color = scolor,
            highlight_color = hcolor,
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                block = Block(position=self.position + mouse.normal)
                blockWD = [block.x, block.y, block.z]
                world.append(blockWD)

            if key == 'right mouse down':
                world.remove([self.x,self.y,self.z])
                destroy(self)


class Map:
    def __init__(self,x, y, z):
        global world

        for zAxis in range(z):
            
            for xAxis in range(x):
                
                for yAxis in range(y):
                    a = yn()
                    if a ==7:
                        y+=1
                    elif a==random.randint(10,seed):
                        y-=1

                    block = Block(sizeY=(1,1,1),position=(xAxis,yAxis,zAxis))
                    blockWD = [block.x,block.y,block.z]
                    world.append(blockWD)

        
#Main render
map = Map(15 , 5, 15)
Sky()
#PLAYER
player = FirstPersonController(position=(1,500,1))
health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=50)
get_WorldData()
app.run()

