class MyArray:
		
    
	def __init__(self,capacity):
		self.array =[None]*capacity
		self.size = 0

	def insert(self,index,elements):
		if index < 0 or index > self.size:
			raise Exception("超出数组实际元素范围！")
		for i in range(self.size,index,-1):
			self.array[i] = self.array[i-1]
		self.array[index] = elements
		self.size += 1
  
	def remove(self,index):
		for i in range(index,self.size):
			self.array[i] = self.array[i+1]
		self.size -= 1
  
	def output(self):
		for i in range(self.size):
			print(self.array[i])

onearray = MyArray(6)

onearray.insert(0, 'a')
onearray.insert(1, 'b')
onearray.insert(2,'c')
onearray.insert(3,100)
onearray.insert(4,'g')
onearray.remove(1)
onearray.output()
