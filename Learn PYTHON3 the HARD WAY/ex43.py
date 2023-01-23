""" from ex43_classes import *

BaseClass = Scene()
BaseClass.enter()
death_scene = Death()
death_scene.enter()
central_corridor = CentralCorridor()
central_corridor.enter()
laser_weapon_armory = LaserWeaponArmory()
laser_weapon_armory.enter()
the_bridge = TheBridge()
escape_pod = EscapePod()

laser_weapon_armory.enter()

mapname = Map("death")
print(mapname.start_scene)
print(mapname.map_name['the_bridge'].enter)
mapname.opening_scene() """

#以上为测试