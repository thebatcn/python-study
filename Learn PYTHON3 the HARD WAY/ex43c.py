# 在运行前或运行后替换
class Parent():

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def altered(self):
        print("Child Befor Parent altered()")
        super(Child, selfi).altered()      #调用父类altered函数
        print("Child After Parent altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()

        