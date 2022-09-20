from threading import Thread
from random import randint
from time import time,sleep

def down_task(filename):
	string = '{)下载完成，耗时了{}秒时间。'
	print('%s下载开始...'%filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('{}下载完成，耗时{}'.format(filename,time_to_download))
	
def main1():
	start = time()
	down_task('阿拉丁')
	down_task('天亮之前')
	end = time()
	
	print('总共耗时{}.'.format(end-start))
    
def main():
	start = time()
	t1 = Thread(target=down_task,args=('阿拉丁',))
	t1.start()
	t2 = Thread(target=down_task,args=('天亮之前',))
	t2.start()
	t1.join()
	t2.join()
	end = time()
	
	print('总共耗时{}.'.format(end-start))
	
if __name__ == '__main__':
	main()
	main1()
	
	

	