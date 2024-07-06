from ursina import *

editor = Ursina()

objects = []
selected_item = ''

def update():
    global selected_item
    if selected_item in objects:
        if selected_item == '{{sky}}':
            selected_item = ''

class Matter(Draggable):
    def __init__(self,id,model='cube',scale=(1,1,1), position=(0,0,0),hcolor=color.blue, color=color.gray,texture=''):
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            texture = texture,
            color = color,
            highlight_color = hcolor,
            scale=scale,
            id = id,
            lock=(1,0,0))
        objects.append(id)


    '''
    def input(self, key):
        global selected_item
        if self.hovered:
            if key == 'left mouse down':
                selected_item = self.id
    '''

class Arrow(Draggable):
    def __init__(self,model='cube',follow=selected_item,scale=(1,1,1), position=(0,0,0),hcolor=color.blue, color=color.gray,texture=''):
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            texture = texture,
            color = color,
            highlight_color = hcolor,
            scale=scale,
            plane_direction=(1,0,0), lock=(1,0,0))
        objects.append(self.id)

    

    def input(self, key):
        global selected_item
        if self.hovered:
            if key == 'left mouse down':
                print("Detected")


sky = Matter(id="{{sky}}", model="sphere", scale=(100,100,100))
cube = Matter(id="cube1",model='cube',hcolor=color.gray)
up_arrow = Arrow(model='arrow',position=(cube.x,cube.y+1,cube.z),hcolor=color.rgb(200,0,0),color=color.red)
cam = EditorCamera()

running = True



editor.run()
