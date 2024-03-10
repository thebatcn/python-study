class Zhan:
    def __init__(self) -> None:
        self._top = None
        self.bottom = None
        self.Data = []
        
    def get_top(self):
        print( len(self.Data)-1)
    
    def insert(self,data):
        self.Data.append(data)
    
zz = Zhan()
zz.get_top()
zz.insert(1)
zz.insert(2)
print(zz.Data)
zz.get_top()
print(zz.Data[1])

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
        
class LinkedZhan:
    def __init__(self) -> None:
        self.size = 0
        self.Top = None
        self.Bottom = None