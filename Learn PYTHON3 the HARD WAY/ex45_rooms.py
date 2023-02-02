"""                                 室内场景类
包括了几个房间的类,基于room类"""


class room():

    # def print_it(self):
    #     print("This is a room.")

    def entry(self):
        print("room's entry()")


class Corridor(room):

    def entry(self):
        print("进入了一小段狭窄的走廊，一端是客厅，另一端是去外面的大门。")


class Living_room(room):

    def entry(self):
        print("这里是客厅。有一台正播放足球比赛的电视在墙上挂着。沙发就是电视的对面。客厅有2处大窗户，餐厅在另一边。")

    def Watch_tv(self):
        print("Watch tv")

    def Dining(self):
        print("Dining")


class Rest_Room(room):

    def entry(self):
        print("Rest_room")

    def go_to_the_toilet(self):
        print("嘘嘘 or 咚咚")


class Study(room):

    def entry(self):
        print("这里是书房")

    def reading(self):
        print("你先看什么书？")


class Bedroom(room):

    def entry(self):
        print("这是一间非常大的卧室")

    def go_to_bed(self):
        print("""是时间睡觉了 
                你进入了梦想。。。。。""")
