from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

in1 = input("This is from input: ")
print(in1)
print('type(first): ',type(first))  #命令行输入的内容的类型是字符串
