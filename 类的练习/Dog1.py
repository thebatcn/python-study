class Dog():
    """模拟小狗的简单测试"""

    def __init__(self,name,age) -> None:
        """初始化属性name和age"""

        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令是坐下"""

        print(self.name.title()+"is now sitting.")

    def roll_over(self):
        """模拟小狗被命令是打滚"""

        print(self.name.title()+"is rolled over!")

dog =Dog("danny",3)

dog.sit()
dog.roll_over()