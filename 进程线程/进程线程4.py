from multiprocessing import Process
import time

def fcn(stt):	
	print(stt)
	time.sleep(2)
	
def main():
	p1 = Process(target=fcn,args=('one',))
	p1.start()
	p2 = Process(target=fcn,args=('two',))
	p2.start()
	p3 = Process(target=fcn,args=('three',))
	p3.start()
	p1.join()
	p2.join()
	p3.join()
	print('e.d')
	
if __name__ == '__main__':
		main()
	