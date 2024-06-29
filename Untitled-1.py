# values = int(input("输入一个数字 >"))
# # match values:
# #     case values if values in [ 1,2,3,4]:
# # 		print(values)
# # 	case _:
# # 		print("Greater than 4!")
# print(values)

mydict = {}
strings = "case values if values in"
print(strings)

for letter in strings:
    mydict.setdefault(letter, 0)
    mydict[letter] += 1
print(mydict)

print(dict(sorted(mydict.items(),key=lambda x: x[1])))