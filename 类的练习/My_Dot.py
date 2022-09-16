"""简单Dot类，属性：位置 X,Y
                 : 大小SIZE
                 :COLOR
方法：返回Dot信息 get_info
    :get_pos(x,y)
    :distance()
    :move(m,n)
"""

import math
import turtle

class My_Dot:
    def __init__(self, x, y, size, color) -> None:
        self.X = x
        self.Y = y
        self.SIZE = size
        self.COLOR = color

    def get_pos(self):
        """返回位置x,y"""
        return (self.X, self.Y)

    def get_info(self):
        """点的属性信息"""
        info = "{}在{}位置，大小是{}，颜色是{}。".format(self.__str__,(self.X, self.Y), self.SIZE, self.COLOR)
        return info

    def move(self,m, n):
        self.X += m
        self.Y += n

    def distance(self,dotobj):

        dist = math.sqrt(pow(abs(dotobj.X-self.X),2)+pow(abs(dotobj.Y-self.Y),2))
        return dist

if __name__=="__main__":

    dot = My_Dot(10, 20, 2, "red")
    dot1 = My_Dot(2,2,20,'white')

    print(dot.COLOR)
    print(dot.get_pos())
    print(dot.get_info())
    
    dot.move(177,80)
    print(dot.get_info())
    dot.move(n=10,m=100)
    print(dot.get_info())
    
    print(dot.distance(dot1))
    dot1.move(30,28)
    print(dot1.distance(dot))

    turtle.screensize(800,600,'red')
    turtle.dot(dot1.SIZE)

    print(dot.get_pos())
    print(dot1.get_pos())
    print(dot1.get_info())