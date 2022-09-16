import time

a = 1000

print('asctime ',time.asctime(time.gmtime()))
print('asctime ',time.asctime())
print('ctime ',time.ctime(a))
print('gmtime ',time.gmtime(a))
print('localtime ',time.localtime(a))
print('time ',time.time())

print('time1 ',time.time())
time.sleep(1)
print('time2 ',time.time())

print(time.strftime('%p%l:%M:%S',time.gmtime(time.time())))