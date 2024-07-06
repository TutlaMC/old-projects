import pygame

class Sprite:
    costumes = ['Sprites/cat/cat.jfif']

    def __init__(self, name, character = 'Sprites/cat/cat.jfif'):
        self.name = name

    def newCostume(self, icon):
        costumes.append(icon)

    def removeCostume(self, name):
        try:
            costumes.remove(name)
        except Exception:
            print('Costume not found')


class Background:
    backgrounds = ['Backgrounds/blank.jfif']
    currentBackgroundNum = 0
    currentBackground = backgrounds[currentBackgroundNum]

    def __init__(self, image='Backgrounds/blank.jfif'):
        self.name = name
        self.image = image

        backgrounds.append(image)

    def nextBackground(self):
        global currentBackgroundNum 
        global currentBackground
        global backgrounds
        currentBackgroundNum+=1
        currentBackground = backgrounds[currentBackgroundNum]

    def previousBackground(self):
        global currentBackgroundNum 
        global currentBackground
        global backgrounds
        currentBackgroundNum-=1
        currentBackground = backgrounds[currentBackgroundNum]

    def gotoBackground(self,name=backgrounds[currentBackgroundNum]):
        global currentBackgroundNum 
        global currentBackground
        global backgrounds
        currentBackgroundNum=backgrounds.index(name)
        currentBackground = backgrounds[name]

