from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
import random

window = Ursina()

#Vars
enemy_spawn_chance = 10

player = FirstPersonController(position=(0,10,0))
sky=Sky()
ground = Entity(model='cube', scale=(100,1,100), color=color.yellow.tint(-.2), texture='white_cube', texture_scale=(100,100), collider='box')
class Enemy(Entity):
    def __init__(self,position=(0,10,0),y=0,x=0,z=0,model='cube',scale=(3,1),color=color.red,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,

            scale=scale,
            y=y,
            x=x,
            z=z,
            position=position

        )


def update():
    num = random.randint(1,2000)
    if num<enemy_spawn_chance:
        en = Enemy(position=(0,10,0))
        e = en.add_script(SmoothFollow(target=player,speed=1))
def input(key):
    print(key)
    # Movement
    if key == 'left shift':
        player.speed +=5
    elif key == 'left shift hold':
        player.speed +=6

    elif not key == 'left shift' or 'left shift hold' or 'space' or 'space up' or 'left shift up' or 'lmeta' or 'lmeta up' or 'shift up' or 'w up' or 'shift':
        player.speed = 3

window.run()