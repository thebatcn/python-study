from multiprocessing import Process
import time
import os

def display():
	print('进程号是{}，这是{}',format(os.getpid()))
	time.sleep(10)
	
def main1():
	start = time.time()
	p1 = Process(target=display)
	p1.start()
	p2 = Process(target=display)
	p2.start()
	p1.join()
	p2.join()
	end = time.time()
	print('用去{}秒',format(end-start))
	
def main():
	start = time.time()
	display()
	display()
	end = time.time()
	print(end-start)
	
	
if __name__ == '__main__':
	main()