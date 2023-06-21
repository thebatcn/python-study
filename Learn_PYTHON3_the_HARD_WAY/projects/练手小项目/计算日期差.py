from datetime import datetime

print("日期格式 年-月-日")
date1 = input("输入开始日期：")
date2 = input("输入结束日期: ")
dalta = (datetime.strptime(date2, "%Y-%m-%d")-datetime.strptime(date1, "%Y-%m-%d")).days

print(dalta)
