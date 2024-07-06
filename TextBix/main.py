from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window = Ursina()
camera.orthographic = True
camera.fov = 10

class killBrick(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.red,collider='box'):
        super().__init__(
            parent=scene,
            scale=scale,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            y=y,
            x=x

        )

class DoubleJump(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )


class JumpPad(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )

class CheckPoint(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(2,0.2),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )





checkpoint=None
checky = None
#Level1
ground = Entity(model='cube', color=color.white33, origin_y=.5, scale=(70, 5, 1), collider='box')
Void = killBrick(model='cube', origin=(-.5,.5), scale=(100,10), x=10, y=-10, collider='box')
killbrick1 = killBrick(model='cube', origin=(-.5,.5), scale=(1,1), x=10, y=2, collider='box')
killbrick1 = killBrick(model='cube', origin=(-.5,.5), scale=(1,1), x=15, y=2, collider='box')
killbrick1 = killBrick(model='cube', origin=(-.5,.5), scale=(1,1), x=20, y=2, collider='box')
dj = DoubleJump(model='cube', origin=(-.5,.5), scale=(1,1), x=25, y=1, collider='box')
checkpoint1 = CheckPoint(model='cube',origin=(-.5,.5),x=30,y=0.1)
checkpoint=3
checky = 1
wall = Entity(model='cube', color=color.white33, origin_y=-.5, scale=(1, 10, 1), y=0, collider='box')




player_controller = PlatformerController2d(scale_y=2, jump_height=4, x=checkpoint)

camera.add_script(SmoothFollow(target=player_controller, offset=[0,1,-30], speed=4))
def killPlayer():
    player_controller.x = checkpoint
    player_controller.y =checky
def double_jump(obj=None):
    if obj is not None:
        obj.enabled=False
        obj.visible=False
    player_controller.jump_height*=2
    player_controller.jump()
    player_controller.x+=2
    player_controller.jump_height=4

def input(key):

    global checkpoint
    global checky
    hit_info = player_controller.intersects()
    if hit_info.hit:
        
        if hit_info.entity.type=='killBrick':
            killPlayer()
        elif hit_info.entity.type=='DoubleJump':
            double_jump(hit_info.entity)
        elif hit_info.entity.type=='JumpPad':
            double_jump()
        elif hit_info.entity.type=='CheckPoint':

            checkpoint = hit_info.entity.x
            checky =hit_info.entity.y
            
        





window.run()