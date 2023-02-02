"""游戏运行"""

import ex45_world
import ex45_rooms
from random import choice

class Maps():
    """用来选择场景"""
    maps = {'corridor': ex45_rooms.Corridor(),
            'living_room': ex45_rooms.Living_room(),
            'rest_room': ex45_rooms.Rest_Room(),
            'study': ex45_rooms.Study(),
            'bedroom': ex45_rooms.Bedroom()}

amap = Maps()
# for a in amap.maps.keys():
#     print(a)

# print(amap.maps['living_room'])

theworld = ex45_world.The_outside_world()
theworld.print_it()
theworld.to_play()

aroom = ex45_rooms.room()
aroom.entry()
b_room = ex45_rooms.Living_room()
b_room.entry()
b_room.Watch_tv()

romm1 = ex45_rooms.Study()
romm1.reading()

amap.maps['living_room']

def afuct(var_one, var_two,
          var_three):
    pass


