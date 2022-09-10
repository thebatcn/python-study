import datetime
import time
from tkinter import ttk

d1 = datetime.datetime.today()
d2 = datetime.datetime.now()

t1 = d2 - d1
print(t1.seconds)

d3 = datetime.timedelta(weeks=1, days=2)
d4 = datetime.timedelta(days=3)
t2 = d3 - d4
print(t2.days)

print(d2.strftime("%Y-%B-%d, %I:%M:%S %p %j %z"))

t = time.localtime()
print(t.__len__())

# time.ctime() 等效于 time.asctime()，返回 时间 str类型
# time.gmtime()、time.localtime(),返回 struct_time 类型  gmtime()没有时区,localtime()有时区

# 可以通过下面方法获取当前时间 
ddn = datetime.datetime.now() 
datetime.datetime.strftime("%H:%M:%S",ddn)

tc =time.localtime()
time.strftime("%H:%M:%S",tc)

# time.localtime()与 time.mktime()功能相反
tt = time.time()
tl = time.localtime(tt)  #struct_time
mt = time.mktime(tl)   #时间截   tt = mt



