class Scene():

	def enter(self):
		print("这是基础场景类")


class Engine():
	
	def __init__(self, Scene_map):
		self.Scene_map = Scene_map


	def play(self):
		print("Engine.play()")		


class Death(Scene):

	def enter(self):
		print("This is Death scene, it is base on Scene.")


class CentralCorridor(Scene):

	def enter(self):
		print("This is CentralCorridor scene, it is base on Scene.")


class LaserWeaponArmory(Scene):

	def enter(self):
		print("This is LaserWeaponArmory scene, it is base on Scene.")


class TheBridge(Scene):

	def enter(self):
		print("This is TheBridge scene, it is base on Scene.")



class EscapePod(Scene):

	def enter(self):
		print("This is EscapePod scene, it is base on Scene.")


class LastScene(Scene):

	def enter(self):
		print("Congratulation, You Win.")



class Map(object):
	"""docstring for Map"""
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
		Map.map_name[self.start_scene].enter()




		