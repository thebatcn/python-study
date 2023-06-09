import time
#time.gmtime()、time.localtime() 获取当前时间 的tuple或者struct_time  结果
#time.strftime(format,tuple)，按照格式转换显示。要时间tuple 或者 struct_time .

a = 1000

# time.asctime([tupletime])接受一个包含9个元素的时间元组作为参数（默认为当前时间），
# 表示年、月、日、时、分、秒、星期、年内第几天和夏令时信息。
# 而time.ctime([secs])接受一个时间戳（默认为当前时间戳）作为参数，表示自UNIX纪元以来的秒数。
print('asctime ', time.asctime(time.gmtime()))       # 获取当前时间字符串
print('asctime ',time.asctime())                    # 获取当前时间字符串
print('ctime()',time.ctime())                       # 获取当前时间字符串
print('ctime ',time.ctime(a))
print('gmtime ',time.gmtime(a))
print('localtime ',time.localtime(a))
print('time ',time.time())

print('time1 ',time.time())
time.sleep(1)
print('time2 ',time.time())

print(time.strftime('%p%H:%M:%S',time.gmtime(time.time())))
