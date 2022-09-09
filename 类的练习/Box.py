class Box:
    """立方体Box类"""
    
    def __init__(self,lenght,width,high) -> None:
        """初始化属性长、宽、高"""

        self.lenght =lenght
        self.width = width
        self.high = high

    def area(self):
        """计算立方体面积"""
        superficial = (self.lenght * self.width + self.lenght * self.high + self.width * self.high)*2
        print(superficial)

    def volume(self):
        """计算体积"""

        print(self.lenght * self.width * self.high)

box1 = Box(5,2,3)
box1.area()
box1.volume()