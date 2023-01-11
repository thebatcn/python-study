from sys import exit

score = float(input("输入你的分数:"))
if not isinstance(score,(int,float)):
    raise ValueError("请输入一个数字")
    exit(0)

if score > 90:
    grade  = "A"
elif 60 < score <= 89:
    grade = "B"
else:
    grade = "C"
print("{} 属于 {}".format(score, grade))

# match score:
#     case 