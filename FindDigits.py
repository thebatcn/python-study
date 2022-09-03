fobj = open("String.txt","r")
num = 0

for line in fobj.readlines():
    for s in line:
        if s.isdigit():
            num += 1 
        
print("There are {} 个数字".format(num))
print(type(line))
