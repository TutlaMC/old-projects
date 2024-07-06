from pyautogui import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar
from ursina.prefabs.editor_camera import EditorCamera
import random
app = Ursina()

random.seed(0)
Entity.default_shader = lit_with_shadows_shader
score=0
ground = Entity(model='plane', collider='box', scale=100, texture='grass', texture_scale=(10,10))
Void = Entity(model='plane', collider='box',color=color.red, scale=1000, y=-10)

editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model='cube', postion=(30,10,20), color=color.orange, origin_y=-.5, speed=8)
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))

gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)
gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)

shootables_parent = Entity()
mouse.traverse_target = shootables_parent
health = 100
hbar = HealthBar(max_value=health,value=health,show_text=True)
game_running =True
def spectate():
    editor_camera.enabled = not editor_camera.enabled

    player.visible_self = editor_camera.enabled
    player.cursor.enabled = not editor_camera.enabled
    gun.enabled = not editor_camera.enabled
    mouse.locked = not editor_camera.enabled
    editor_camera.position = player.position

    application.paused = editor_camera.enabled
def take_damage(number):
    global health
    global game_running
    global player
    global ground
    global gun
    global score
    
    chance = random.randint(1,100)
    if number>health:
        print('Game Over')
        destroy(hbar)
        destroy(gun)
        spectate()
        def close():
            destroy(a)
        def rerun():
            pass
        txt = 'Game Over! \n Score: '
        txt=txt+str(score)+'\n'
        with open('C:\\Users\\Admin\\OneDrive\\Desktop\\Tutla\\PythonProjects\\Gun Game\\beta 1.2\\score.txt') as scr:
            
            hscr = scr.read()
            if score> int(hscr):
                with open('C:\\Users\\Admin\\OneDrive\\Desktop\\Tutla\\PythonProjects\\Gun Game\\beta 1.2\\score.txt','w') as scr:
                    scr.write(str(score))
                    hscr = score
            txt = txt+'High Score: '+str(hscr)+'\nClick Here to spectate world!'
       
        a = Button(text=txt,scale=0.5)

        a.on_click = close
        #b = Button(text='Click me to Play Again!',scale=0.2)

        #b.on_click = rerun
        player.position=(1000,-10,10)
        

        game_running=False
        
        
    else:
        if chance<10:
            health-=number
            hbar.value = health
    
        
    
for i in range(16):
    Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1,2),
        x=random.uniform(-8,8),
        z=random.uniform(-8,8) + 8,
        collider='box',
        scale_y = random.uniform(2,3),
        color=color.hsv(0, 0, random.uniform(.9, 1))
        )

def update():
    global health
    if held_keys['left mouse']:
        shoot()
    if Void.intersects(player):
        print('Player fell into Void')
        take_damage(1)

def shoot():
    if not gun.on_cooldown:
        # print('shoot')
        gun.on_cooldown = True
        gun.muzzle_flash.enabled=True
        from ursina.prefabs.ursfx import ursfx
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
        invoke(gun.muzzle_flash.disable, delay=.05)
        invoke(setattr, gun, 'on_cooldown', False, delay=.15)
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
            mouse.hovered_entity.hp -= 10
            mouse.hovered_entity.blink(color.red)


from ursina.prefabs.health_bar import HealthBar

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=shootables_parent, model='cube', scale_y=2, origin_y=-.5, color=color.light_gray, collider='box', **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        global player
        global game_running
        

        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return
        if self.intersects(player).hit:
            take_damage(1)
        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


        #self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 5

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        global enemies
        self._hp = value
        if value <= 0:
            global score
            score+=2
            destroy(self)
            chance = random.randint(1,10)
            if chance<10:
                print('new')
                enemies = [Enemy(x=x*4) for x in range(3)]
                for i in enemies:
                    i.add_script(SmoothFollow(target=player,speed=0.5))

            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1

# Enemy()
enemies = [Enemy(x=x*4) for x in range(4)]


def pause_input(key):
    global game_running
    if game_running:
        if key == 'left shift':
            player.speed +=5
        elif key == 'left shift hold':
            player.speed +=6

        elif not key == 'left shift' or 'left shift hold' or 'space' or 'space up' or 'left shift up' or 'lmeta' or 'lmeta up' or 'shift up' or 'w up' or 'shift':
            player.speed = 3
    if key == 'tab':
        if False:
            
            editor_camera.enabled = not editor_camera.enabled

            player.visible_self = editor_camera.enabled
            player.cursor.enabled = not editor_camera.enabled
            gun.enabled = not editor_camera.enabled
            mouse.locked = not editor_camera.enabled
            editor_camera.position = player.position

            application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)


sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()

app.run()