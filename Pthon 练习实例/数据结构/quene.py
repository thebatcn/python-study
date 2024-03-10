# 初始化队列
class Myquene:
    def __init__(self,capacity) -> None:
        self.list = [None]*capacity
        self.front = 0
        self.rear = 0
        
    # 入队
    def enqueue(self,element):
        if (self.rear + 1) % len(self.list) == self.front:
            raise Exception("队列已满。")
        self.list[self.rear] = element
        self.rear = (self.rear + 1)%len(self.list)
        
    # 出队
    def dequeue(self):
        if self.rear == self.front:
            raise Exception("队列已满。")
        dequeue_element = self.list[self.front]
        self.front = (self.front + 1) % len(self.list)
        return dequeue_element
    
    # 输出队列
    def output(self):
        i = self.front
        while i != self.rear:
            print(self.list[i])
            i = (i+1)%len(self.list)
        

onequeue = Myquene(6)
onequeue.enqueue(3)
onequeue.enqueue('af')
onequeue.enqueue(9)
onequeue.enqueue(0)
onequeue.enqueue('ha')

onequeue.output()
print(onequeue.dequeue())
onequeue.output()

