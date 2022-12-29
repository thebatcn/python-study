import time
#time.gmtime()、time.localtime() 获取当前时间 的tuple或者struct_time  结果
#time.strftime(format,tuple)，按照格式转换显示。要时间tuple 或者 struct_time .

a = 1000

print('asctime ',time.asctime(time.gmtime()))       # 获取当前时间字符串
print('asctime ',time.asctime())                    # 获取当前时间字符串
print('ctime()',time.ctime())                       # 获取当前时间字符串
print('ctime ',time.ctime(a))
print('gmtime ',time.gmtime(a))
print('localtime ',time.localtime(a))
print('time ',time.time())

print('time1 ',time.time())
time.sleep(1)
print('time2 ',time.time())

print(time.strftime('%p%l:%M:%S',time.gmtime(time.time())))
