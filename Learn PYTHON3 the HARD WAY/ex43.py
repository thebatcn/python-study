from sys import exit
from random import randint
from textwrap import dedent


class Scene():
    
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)



class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map
        print("Engine.play()")


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):
    
    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass



class EscapePod(Scene):

    def enter(self):
        pass


class LastScene(Scene):

    def enter(self):
        pass


class Map(object):
    """docstring for Map."""

    map_name ={"death":Death, "central_corridor":CentralCorridor,
				"laser_weapon_armory":LaserWeaponArmory,
				"the_bridge":TheBridge,
				"escape_pod":EscapePod,
				"lastscene":LastScene}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        pass
    def opening_scene(self):
        pass

       

