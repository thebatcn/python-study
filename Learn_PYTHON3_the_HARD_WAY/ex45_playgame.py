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
            'bedroom': ex45_rooms.Bedroom(),
            'finish': ex45_rooms.Finish()}

    def __init__(self, start_scene):
        self.start_scene_name = start_scene

    def next_scene(self, scene_name):
        val = self.maps.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene_name)

class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        # last_scene = self.scene_map.next_scene('finish')

        # while current_scene != last_scene:
        #     next_scene_name = current_scene.entry()
        #     current_scene = self.scene_map.next_scene(next_scene_name)  

        current_scene.entry()

#  引擎理解       

# 切换场景类

# 1、字典 {名字：场景类}     2、初始化Map类，参数为”场景名字”
# 3、
# 函数 next_map(场景名字）
# 返回 val = 字典[场景名字] 类

# 4、函数 open_map
# 返回
# next_map(场景名字）





# 具体场景类

# 函数  enter()，返回  string 作为  场景名字


# Engine  
# Engine 包含 Map类

# 函数  paly()  调用 enter()运行

amap = Maps('study')
play = Engine(amap)
play.play()
# for a in amap.maps.keys():
#     print(a)

# print(amap.maps['living_room'])

# theworld = ex45_world.The_outside_world()
# theworld.print_it()
# theworld.to_play()

# aroom = ex45_rooms.Bedroom()
# aroom.entry()
# b_room = ex45_rooms.Living_room()
# b_room.entry()
# b_room.Watch_tv()

# romm1 = ex45_rooms.Study()
# romm1.reading()

# amap.maps['living_room']

# def afuct(var_one, var_two,
#           var_three):
#     pass
# aroom.go_to_bed()

