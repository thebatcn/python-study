class Velicle:
    """交通工具类"""

    def __init__(self,speed,size) -> None:
        
        self.__speed = speed
        self.size = size
        
    def move(self,s):
        """计算移动的距离"""

        self.distance =  self.__speed * s
        return self.distance

    def setspeed(self,speed):
        """设置速度"""

        self.__speed = speed

    def speedUp(self):
        """加速"""

        self.__speed += 10
       

    def speedDown(self):
        """减速"""

        self.__speed -= 10

    
mycar = Velicle(30,1)
print(mycar.move(100))

mycar.setspeed(50)
print(mycar.move(100))

mycar.speedUp()
print(mycar.move(100))
