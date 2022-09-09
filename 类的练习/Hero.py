""" 定义一个Hero类 """
""" 属性有 power,name，分别代表体力值和英雄的名子，体力值默认为100； """
""" 方法有 """
""" 1.) go() //行走的方法，如果体力值为0，则输出不能行走，此英雄已死亡的信息 """
""" 2.) eat(int n); //吃的方法，参数是补充的血量，将 n的值加到属性power中，power的值最大为10 """
""" 3.) hurt();//每受到一次伤害，体力值－10，体力值最小不能小于0 """
""" ———————————————— """
""" 版权声明：本文为CSDN博主「老呂」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处 """
""" 原文链接：https://blog.csdn.net/qq_42115732/article/details/86626960 """

class Hero:
    """Hero简单类"""

    def __init__(self,name,power) -> None:
        """初始化name、power属性"""

        self.name = name
        self.power = power
        
    