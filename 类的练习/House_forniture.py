"""
class House：
	area
	type
	forniture[]
	add_item()
	has_area()
	__str__:（户型、面积、剩余面积、家具名称）

class Forniture:
	name
	area
"""

class House:
	"""House类，有户型、面积、家具名称"""

	def __init__(self,house_type,area) -> None:
		"""初始化属性 户型、面积、家具名称"""
		
		self.type = house_type
		self.area = area
		self.remain_area = area
		self.forniture = []

	def add_item(self,forniture):
		"""添加家具"""
		#如果家具占地面积大于房屋空闲面积，提示错误。

		if forniture.area > self.remain_area:
			print("家具太大，房间放不下。")
		else:
			self.forniture.append(forniture.name)
			self.remain_area -= forniture.area

	def has_area(self):
		"""房屋剩余面积"""

		return self.remain_area


	def __str__(self) -> str:
		"""显示房屋的情况"""

		return("这是{0}的房子，总面积是{1}平方米，目前已经摆放了{2}这些家具。房屋还剩余{3}面积。".format(self.type,self.area,
																					str(self.forniture),self.remain_area))

class Forniture:
	"""家具类"""

	def __init__(self,name,area) -> None:
		"""初始化属性name:家具名称，area:占地面积"""

		self.name = name 
		self.area =area

		pass

myhouse = House("三室一厅",101)
bed = Forniture("bed",4)
chest = Forniture('chest',2)
table = Forniture("table",1.5)
big = Forniture("Big",200)
myhouse.add_item(bed)
myhouse.add_item(chest)
myhouse.add_item(table)
myhouse.add_item(big)
print(myhouse.__str__())

