from ursina import *
from ursina.models.procedural.terrain import Terrain

e = Entity(model=Terrain('heightmap_1', skip=16), scale=(20,5,20))
EditorCamera()
