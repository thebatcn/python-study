fobj = open("String.txt","r")
num = 0

for line in fobj.readlines():
    for s in line:
        if s.isdigit():
            num += 1 
        
print("There are {} ge shuzhi".format(num))
print(type(line))
