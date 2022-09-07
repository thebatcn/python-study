class Person:
    """简单的Person类"""

    def __init__(self,name,weight) -> None:
        """初始化属性name和weight"""

        self.name = name
        self.weight = weight

    def eat(self):
        """吃东西，增加体重."""

        print(self.name.title() + "在吃东西。")
        self.weight += 1

    def run(self):
        """跑步，减少体重。"""

        print(self.name.title() + "在跑步锻炼。")
        self.weight -= 0.5
    
    def get_weight(self):
        """获取体重"""

        return self.weight


xiaoming = Person('xiaoming',75)
print(xiaoming.get_weight())
xiaoming.run()
print(xiaoming.get_weight())
xiaoming.eat()
print(xiaoming.get_weight())

xiaomei = Person('xiaomei',45)
print(xiaomei.get_weight())
xiaomei.eat()
print(xiaomei.get_weight())