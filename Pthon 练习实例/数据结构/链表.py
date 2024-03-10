class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.last = None
        
    def get(self,index):
        if index <0 or index >= self.size:
            raise Exception("超出链表节点访问！")
        p = self.head
        
        for i in range(index):
            p=p.next
        return p
    
    def insert(self,data,index):
        if index <0 or index > self.size:
            raise Exception("超出链表节点访问！")
        node = Node(data)
        if self.size == 0:
            #空链表
            self.head = node
            self.last = node
        elif index == 0:
            #插入头部
            node.next = self.head
            self.head = node
        elif self.size == index:
            #插入尾部
            self.last.next = node
            self.last = node
        else:
            #插入中间
            pre_node = self.get(index - 1)
            node.next = pre_node.next
            pre_node.next = node
        self.size += 1
    
    
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点访问！")
        # 暂存被删除的节点，用于返回
        if index == 0:
            #删除头节点
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            #删除尾节点
            prev_node  = self.get(index-1)
            remove_node = prev_node.next
            prev_node.next = None
            self.last = prev_node
        else:
            #删除中间节点
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            remove_node = prev_node.next
            prev_node.next = next_node
            
    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
            
    # def Size(self):
    #     return self.Size

mylink = LinkedList()

mylink.insert(42,0)
print("hedad = {} last = {}".format(mylink.head,mylink.last))
# mylink.output()
mylink.insert(23,1)
print("hedad = {} last = {}".format(mylink.head,mylink.last))
# mylink.output()
mylink.insert(10,2)
print("hedad = {} last = {}".format(mylink.head,mylink.last))
mylink.insert(70,2)
# mylink.output()
# print(mylink.size)
mylink.remove(3)
# mylink.output()
mylink.insert('abc',2)
for i in range(5):
    mylink.insert(i,i+1)
mylink.output()