import numpy as np
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.prefabs.health_bar import HealthBar
import random
from perlin_noise import PerlinNoise

app = Ursina()
terrain = Entity(model=None,collider=None)

#PLAYER
grasNum = 0
stoneNum = 0
woodNum = 0
def classifyBlock(block):
    if block.color == color.green:
        return 'Grass'
    elif block.color == color.light_gray:
        return 'Stone'
    elif block.color == color.brown:
        return 'Wood'
    elif block.color == color.white: return 'snow'



world = []
def get_WorldData():
    
    return world
class Inventory(Entity):
    objects = []
    prevIt = None
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            texture = 'white_cube',
            texture_scale = (5,8),
            scale = (.5, .8),
            origin = (-.5, .5),
            position = (-.3,.4),
            color = color.color(0,0,.1,.9),
            )

        for key, value in kwargs.items():
            setattr(self, key, value)


    def find_free_spot(self):
        for y in range(8):
            for x in range(5):
                grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in self.children]
                print(grid_positions)

                if not (x,-y) in grid_positions:
                    print('found free spot:', x, y)
                    return x, y


    def append(self, item,ccolor=color.green, yt=False,x=0, y=0):
        print('add item:', item)

        if len(self.children) >= 5*8:
            print('inventory full')
            error_message = Text('<red>Inventory is full!', origin=(0,-1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()
        if yt:

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1/self.texture_scale[0],
                scale_y = 1/self.texture_scale[1],
                origin = (-.5,.5),
                x = x * 1/self.texture_scale[0],
                y = -y * 1/self.texture_scale[1],
                z = -.5,
                )
        else:
              icon = Draggable(
                parent = self,
                model = 'quad',
                color = ccolor,
                scale_x = 1/self.texture_scale[0],
                scale_y = 1/self.texture_scale[1],
                origin = (-.5,.5),
                x = x * 1/self.texture_scale[0],
                y = -y * 1/self.texture_scale[1],
                z = -.5,
                )  
        name = item.replace('_', ' ').title()

        

        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0,0,0,.8)


        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01   # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int((icon.x + (icon.scale_x/2)) * 5) / 5
            icon.y = int((icon.y - (icon.scale_y/2)) * 8) / 8
            icon.z += .01

            # if outside, return to original position
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            # if the spot is taken, swap positions
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop

inventory = Inventory()
inventory.visible=False
def BlockToInventory(block):
    inventory.append(classifyBlock(block),ccolor=block.color)
    if block.color == color.green:
        
        return 'grass'
        
    elif block.color == color.light_gray:
        
        return 'stone'
    elif block.color == color.brown:
        return 'wood'
    elif block.color == color.white: return 'snow'
    

player = FirstPersonController(position=(20,100,1))
class Block(Button):
    def __init__(self,parent=scene,sizeY=(1,1,1),position=(1,1,1),texture='grass',hcolor=color.lime, scolor=color.green):
        super().__init__(
            parent = parent,
            position=position,
            model = 'cube',
            origin_y = .5,
            size = sizeY,
            texture = texture,
            color = scolor,
            highlight_color = hcolor,
        )


    def input(self, key):
        global invtOC
        global inventory
        player_pos = player.position
        if self.hovered:
            if key == 'left mouse down':
                block = Block(position=self.position + mouse.normal,scolor=self.color)
                blockWD = [block.x, block.y, block.z]
                print(blockWD)
                world.append(blockWD)

            if key == 'right mouse down':
                world.remove([self.x,self.y,self.z])
                BlockToInventory(self)
                destroy(self)
        
        if key=='e':
            
            inventory.visible = True
            mouse.visible = True
            player.enabled = False
            for i in inventory.children:
               i.tooltip.visible = True
        elif key == 'r':
            inventory.visible = False
            mouse.visible = False
            player.enabled = True
            for i in inventory.children:
               i.tooltip.visible = False
        
def stb(pv,nposition):
    global world
    block = Block(position=(nposition[0],nposition[1],nposition[2]))
    blockWD = [nposition[0],nposition[1],nposition[2]]
    world.append(blockWD)

class Animal():
    Body = Entity(model='cube',position=(random.randint(1,20),10,random.randint(10,15)))

class Tree():
    def __init__(self,xt,yt,zt):
        pv = None
        for i in range(3):
            Block(position=(xt,yt+i,zt),hcolor=color.brown,scolor=color.brown)
            pv = [xt,yt+i,zt]
            blockWD =pv
            world.append(blockWD)
            
        stb(pv,nposition=(pv[0],pv[1]+1,pv[2]))
        stb(pv,nposition=(pv[0]+1,pv[1]+1,pv[2]))
        stb(pv,nposition=(pv[0]-1,pv[1]+1,pv[2]))
        stb(pv,nposition=(pv[0],pv[1]+1,pv[2]-1))
        stb(pv,nposition=(pv[0],pv[1]+1,pv[2]+1))
        stb(pv,nposition=(pv[0]+1,pv[1]+1,pv[2]+1))
        stb(pv,nposition=(pv[0]-1,pv[1]+1,pv[2]+1))




class ChunkBuild:
    def __init__(self,noise,terrain_width,type='normal',texture='grass',freq=24,xtin=0,amp=5,ac=color.green,cut=0):
        global world
        
        for i in range(terrain_width*terrain_width):
           
            x = floor(i/terrain_width)
            z=floor(i%terrain_width)
            y = floor(noise([x/freq,z/freq])*amp)-cut
            block = Block(sizeY=(1,1,1),scolor=ac,texture=texture,position=(x+xtin,y,z))
            block.parent = terrain
            blockWD = [block.x,block.y,block.z]
            world.append(blockWD)
            if type=='normal':
                a = random.randint(0,280)
                
                if a>275:
                    Tree(xt=x+xtin,yt=y+1,zt=z)

        

                    
tw =20

                    
class Chunk:
    def __init__(self,type='plain',xtin=0):
        
        global tw
        noise = PerlinNoise(octaves=2,seed=random.randint(0,100))
        ct=1
        if type == 'plain':
            chunk = ChunkBuild(noise,tw,xtin=xtin)
            for i in range(int(tw/4)):
                grd1=ChunkBuild(noise,tw,type='underground',ac=color.light_gray,cut=ct,xtin=xtin)
                ct+=1
        elif type=='desert':
            chunk = ChunkBuild(noise,tw,ac=color.yellow,xtin=xtin)
            for i in range(int(tw/4)):
                grd1=ChunkBuild(noise,tw,type='underground',ac=color.light_gray,cut=ct,xtin=xtin)
                ct+=1
        elif type == 'mountains': 
             chunk = ChunkBuild(noise,tw,ac=color.yellow,xtin=xtin)
             for i in range(int(tw/4)):
                grd1=ChunkBuild(noise,tw,type='underground',ac=color.light_gray,cut=ct,xtin=xtin)
                ct+=1
             ct=1
             for i in range(5):
                grd1=ChunkBuild(noise,tw,type='mountains',ac=color.white,texture=None,cut=ct,xtin=xtin)
                ct-=1



#Main render
Chunk()
Chunk(xtin=tw,type='desert')

Sky()

#EditorCamera()
health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=50)
get_WorldData()


app.run()

