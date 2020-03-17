import json


d={}


myfile =open('dzp1.txt','r')

'''
name=input("输入名字：")
age=input("输入年龄:")
addrest=input('输入地址:')




d.update({name:[age,addrest]})

jsobj=json.dumps(d)
myfile.write(jsobj+'\n')

'''
for  line in myfile.readlines():
	jsobj=json.loads(line)
	d.update(jsobj)
	
print(d)
print(d['huting'])
myfile.close
